from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from users.decorators import admin_required

@staff_member_required
def order_list(request):
    orders = Order.objects.all()
    return render(request, "orders/order_list.html", {"orders": orders})

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, "orders/order_detail.html", {"order": order})

@login_required
@admin_required
def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()

            # محاسبه قیمت
            total = sum(food.price for food in order.foods.all())
            order.total_price = total
            order.save()

            return redirect("order_list")
    else:
        form = OrderForm()

    return render(request, "orders/order_create.html", {"form": form})

