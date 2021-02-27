from django.shortcuts import render
from .models import Product
from .forms import Productform

def product_view(request):
    if request.method == "POST":
        form = Productform(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'products/product.html', {})
    else:
        return render(request, 'products/products.html', {})
