from django.shortcuts import render, redirect
from .models import User
from .forms import Userform
from users.models import User


def register_view(request):
    if request.method == "POST":
        form = Userform(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect(request, 'users:login')
    else:
        form = Userform()
    return render(request, 'users/register.html', {})


def login_view(request):
    return render(request,'users/login.html', {})
