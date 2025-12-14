from django.shortcuts import render
from .models import Table
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.is_authenticated and user.role == "admin"

@login_required
@user_passes_test(is_admin)
def table_list(request):
    tables = Table.objects.all()
    return render(request, "tables/list.html", {"tables": tables})


