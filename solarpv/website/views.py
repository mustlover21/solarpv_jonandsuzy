from django.shortcuts import render

def home_view(request):
    return render(request, "index.html", {})
def about_view(request):
    return render(request, "about.html", {})
def contact_view(request):
    return render(request, "contact.html", {})
def modules_view(request):
    return render(request, "modules.html", {})
def cyber_view(request):
    return render(request, "cyber.html", {})
def data_view(request):
    return render(request, "data.html", {})
def landing_view(request):
    return render(request, "landing.html", {})
def landing2_view(request):
    return render(request, "landing2.html", {})
def password_view(request):
    return render(request, "password.html", {})
def portal_view(request):
    return render(request, "portal.html", {})
def privacy_view(request):
    return render(request, "privacy.html", {})
def randt_view(request):
    return render(request, "randt.html", {})
def sitemap_view(request):
    return render(request, "sitemap.html", {})
def systems_view(request):
    return render(request, "systems.html", {})
def tandc_view(request):
    return render(request, "tandc.html", {})
def registered_view(request):
    return render(request, "registered.html", {})
