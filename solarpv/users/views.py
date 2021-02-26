from django.shortcuts import render
from .models import User
from .forms import Userform

def register(request):
    if request.method == "POST":
        form = Userform(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'users/register.html', {})
    else:
        return render(request, 'users/register.html', {})
