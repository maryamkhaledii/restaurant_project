from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required

@login_required
def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, "reservations/list.html", {"reservations": reservations})

@login_required
def reservation_create(request):
    form = ReservationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("home")
    return render(request, "reservations/create.html", {"form": form})


