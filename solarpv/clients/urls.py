from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [
    path('newclient/', views.newclient, name='newclient'),
]
