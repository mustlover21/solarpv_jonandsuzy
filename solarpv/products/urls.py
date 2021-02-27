from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('product/', views.product_view, name='product'),
]
