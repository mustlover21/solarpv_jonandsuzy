from django.shortcuts import render
from .models import Client
from .forms import Clientform

def newclient_view(request):
    if request.method == "POST":
        form = Clientform(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'clients/newclient.html', {})
    else:
        return render(request, 'clients/newclient.html', {})
