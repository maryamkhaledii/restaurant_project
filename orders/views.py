from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from foods.models import Food
from .cart import Cart

@login_required
def order_create(request):
    cart = Cart(request)

    if not cart.cart:
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


#  لیست سفارش‌های کاربر
@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "orders/list.html", {"orders": orders})


#  جزئیات سفارش
@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, "orders/detail.html", {"order": order})


#  لیست سفارش‌ها برای ادمین
@login_required
def admin_order_list(request):
    if not request.user.is_staff:
        return redirect("home")

    orders = Order.objects.all().order_by("-created_at")
    return render(request, "orders/admin_list.html", {"orders": orders})

