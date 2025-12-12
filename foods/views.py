from django.shortcuts import render, redirect, get_object_or_404
from .models import Food
from .forms import FoodForm

def food_list(request):
    foods = Food.objects.all()
    return render(request, "foods/food_list.html", {"foods": foods})

def food_detail(request, pk):
    food = get_object_or_404(Food, pk=pk)
    return render(request, "foods/food_detail.html", {"food": food})

def food_create(request):
    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("food_list")
    else:
        form = FoodForm()
    return render(request, "foods/food_create.html", {"form": form})

