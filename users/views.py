from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()   # 👈 فقط برای register


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
        messages.error(request, "نام کاربری یا رمز عبور اشتباه است")

    return render(request, "users/login.html")


def user_logout(request):
    logout(request)
    return redirect("home")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            return render(request, "users/register.html", {
                "error": "رمز عبور و تکرار آن یکسان نیست"
            })

        if User.objects.filter(username=username).exists():
            return render(request, "users/register.html", {
                "error": "این نام کاربری قبلاً ثبت شده"
            })

        user = User.objects.create_user(
            username=username,
            password=password1,
            role="customer"
        )

        login(request, user)
        return redirect("home")

    return render(request, "users/register.html")
