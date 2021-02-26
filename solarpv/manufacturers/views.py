from django.shortcuts import render
from .models import Manufacturer
from .forms import Manufacturerform

def manufacturer(request):
    if request.method == "POST":
        form = Manufacturerform(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'manufacturers/manufacturer.html', {})
    else:
        return render(request, 'manufacturers/manufacturer.html', {})
