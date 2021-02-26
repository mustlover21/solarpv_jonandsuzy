from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'manufacturers'

urlpatterns = [
    path('manufacturer/', views.manufacturer, name='manufacturer'),
]
