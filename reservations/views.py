from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.decorators import customer_required, admin_required
from .models import Reservation
from .forms import ReservationForm
from django.contrib import messages


# 👤 رزرو میز (مشتری)
@login_required
@customer_required
def reservation_create(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            table = form.cleaned_data["table"]
            date = form.cleaned_data["date"]
            time = form.cleaned_data["time"]

            exists = Reservation.objects.filter(
                table=table,
                date=date,
                time=time,
                status="pending"
            ).exists()

            if exists:
                messages.error(request, "❌ این میز در این زمان قبلاً رزرو شده")
            else:
                reservation = form.save(commit=False)
                reservation.user = request.user
                reservation.save()
                messages.success(request, "✅ رزرو با موفقیت ثبت شد")
                return redirect("home")
    else:
        form = ReservationForm()

    return render(request, "reservations/create.html", {"form": form})


# 👨‍💼 لیست رزروها (ادمین)
@login_required
@admin_required
def reservation_admin_list(request):
    reservations = Reservation.objects.all().order_by("-created_at")
    return render(request, "reservations/admin_list.html", {
        "reservations": reservations
    })


# ❌ لغو رزرو (ادمین)
@login_required
@admin_required
def reservation_cancel(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    reservation.status = "cancelled"
    reservation.save()
    messages.success(request, "❌ رزرو لغو شد")
    return redirect("reservations:admin_list")


# ✅ انجام شده (ادمین)
@login_required
@admin_required
def reservation_done(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    reservation.status = "done"
    reservation.save()
    messages.success(request, "✅ رزرو انجام شد")
    return redirect("reservations:admin_list")




