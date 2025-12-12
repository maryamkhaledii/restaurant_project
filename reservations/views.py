from django.shortcuts import render, get_object_or_404, redirect
from .models import Reservation
from .forms import ReservationForm

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, "reservations/reservation_list.html", {"reservations": reservations})

def reservation_detail(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    return render(request, "reservations/reservation_detail.html", {"reservation": reservation})

def reservation_create(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("reservation_list")
    else:
        form = ReservationForm()
    return render(request, "reservations/reservation_create.html", {"form": form})

def reservation_update(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == "POST":
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect("reservation_detail", pk=pk)
    else:
        form = ReservationForm(instance=reservation)
    return render(request, "reservations/reservation_update.html", {"form": form})

def reservation_delete(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == "POST":
        reservation.delete()
        return redirect("reservation_list")
    return render(request, "reservations/reservation_delete.html", {"reservation": reservation})

