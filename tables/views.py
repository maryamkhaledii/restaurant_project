from django.shortcuts import render, get_object_or_404, redirect
from .models import Table
from users.decorators import admin_required
from django.contrib import messages


@admin_required
def table_list(request):
    tables = Table.objects.all()
    return render(request, "tables/list.html", {"tables": tables})


@admin_required
def table_detail(request, pk):
    table = get_object_or_404(Table, pk=pk)
    return render(request, "tables/detail.html", {"table": table})


@admin_required
def table_create(request):
    if request.method == "POST":
        number = request.POST.get("number")
        capacity = request.POST.get("capacity")

        if Table.objects.filter(number=number).exists():
            messages.error(request, "این شماره میز قبلاً ثبت شده")
        else:
            Table.objects.create(number=number, capacity=capacity)
            messages.success(request, "میز با موفقیت اضافه شد")
            return redirect("tables:list")

    return render(request, "tables/create.html")


@admin_required
def table_update(request, pk):
    table = get_object_or_404(Table, pk=pk)

    if request.method == "POST":
        table.number = request.POST.get("number")
        table.capacity = request.POST.get("capacity")
        table.save()
        messages.success(request, "میز ویرایش شد")
        return redirect("tables:list")

    return render(request, "tables/update.html", {"table": table})


@admin_required
def table_delete(request, pk):
    table = get_object_or_404(Table, pk=pk)

    if request.method == "POST":
        table.delete()
        messages.success(request, "میز حذف شد")
        return redirect("tables:list")

    return render(request, "tables/delete.html", {"table": table})