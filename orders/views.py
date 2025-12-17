from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from foods.models import Food


@login_required
def order_create(request):
    cart = getattr(request, "cart", None)

    if not cart or len(cart) == 0:
        return redirect("foods:menu")

    total_price = 0
    for item in cart:
        total_price += item["price"] * item["quantity"]

    order = Order.objects.create(
        user=request.user,
        total_price=total_price,
        status="pending"
    )

    for item in cart:
        food = get_object_or_404(Food, id=item["food_id"])
        OrderItem.objects.create(
            order=order,
            food=food,
            price=item["price"],
            quantity=item["quantity"]
        )

    cart.clear()

    return redirect("orders:success", order.id)


@login_required
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, "orders/success.html", {"order": order})


@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "orders/list.html", {"orders": orders})


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, "orders/detail.html", {"order": order})
