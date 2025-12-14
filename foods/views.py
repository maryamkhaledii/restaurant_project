from django.shortcuts import render, redirect, get_object_or_404
from .models import Food
from .forms import FoodForm
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.is_authenticated and user.role == "admin"

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Food

@login_required
def food_list(request):
    foods = Food.objects.all()
    return render(request, "foods/list.html", {"foods": foods})

@login_required
@user_passes_test(is_admin)
def food_create(request):
    form = FoodForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("foods:list")
    return render(request, "foods/create.html", {"form": form})


def food_detail(request, pk):
    food = get_object_or_404(Food, pk=pk)
    return render(request, "foods/detail.html", {"food": food})



