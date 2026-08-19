from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Service
from .forms import AppointmentForm


def home(request):
    services = Service.objects.all()

    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your appointment has been booked successfully!")
            return redirect("home")
    else:
        form = AppointmentForm()

    context = {
        "services": services,
        "form": form,
    }

    return render(request, "scheduler/home.html", context)