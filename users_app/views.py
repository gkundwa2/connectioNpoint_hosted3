
from django.shortcuts import render, redirect
from .forms import CustomRegisterForm
from django.contrib import messages
from ConnectionApp.automatic_reset_verified import auto_reset
from django.contrib.auth.decorators import login_required


@login_required
def register(request):
    auto_reset()
    if request.method == "POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(
                request, ("New User Account Has Been Created in Connection Point System!"))
            return redirect('listpage')

    else:
        register_form = CustomRegisterForm()
    return render(request, 'register.html', {'register_form': register_form})
