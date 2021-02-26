from django.shortcuts import render

def home(request):
    return render(request, "index.html", {})
def about(request):
    return render(request, "about.html", {})
def contact(request):
    return render(request, "contact.html", {})
def login(request):
    return render(request, "login.html", {})
def modules(request):
    return render(request, "modules.html", {})
def cyber(request):
    return render(request, "cyber.html", {})
def data(request):
    return render(request, "data.html", {})
def landing(request):
    return render(request, "landing.html", {})
def landing2(request):
    return render(request, "landing2.html", {})
def password(request):
    return render(request, "password.html", {})
def portal(request):
    return render(request, "portal.html", {})
def privacy(request):
    return render(request, "privacy.html", {})
def randt(request):
    return render(request, "randt.html", {})
def register2(request):
    return render(request, "register2.html", {})
def sitemap(request):
    return render(request, "sitemap.html", {})
def systems(request):
    return render(request, "systems.html", {})
def tandc(request):
    return render(request, "tandc.html", {})
def registered(request):
    return render(request, "registered.html", {})
def logout(request):
    return render(request, "logout.html", {})
