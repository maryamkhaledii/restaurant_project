from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from users.decorators import admin_required, customer_required
from .models import Food
from .forms import FoodForm


# منو برای مشتری
@login_required
@customer_required
def menu(request):
    foods = Food.objects.all()
    return render(request, "foods/menu.html", {"foods": foods})


#  لیست غذا برای مدیر
@login_required
@admin_required
def food_admin_list(request):
    foods = Food.objects.all()
    return render(request, "foods/admin_list.html", {"foods": foods})


#  افزودن غذا
@login_required
@admin_required
def food_create(request):
    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("foods:admin_list")
    else:
        form = FoodForm()

    return render(request, "foods/create.html", {"form": form})


# جزئیات غذا (اختیاری)
@login_required
def food_detail(request, pk):
    food = get_object_or_404(Food, pk=pk)
    return render(request, "foods/detail.html", {"food": food})




