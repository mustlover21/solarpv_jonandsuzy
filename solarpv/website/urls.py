from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('cyber/', views.cyber, name='cyber'),
    path('data/', views.data, name='data'),
    path('login/', views.login, name='login'),
    path('landing/', views.landing, name='landing'),
    path('landing2/', views.landing2, name='landing2'),
    path('modules/', views.modules, name='modules'),
    path('password/', views.password, name='password'),
    path('portal/', views.portal, name='portal'),
    path('privacy/', views.privacy, name='privacy'),
    path('randt/', views.randt, name='randt'),
    path('register2/', views.register2, name='register2'),
    path('registered/', views.registered, name='registered'),
    path('sitemap/', views.sitemap, name='sitemap'),
    path('systems/', views.systems, name='systems'),
    path('tandc/', views.tandc, name='tandc'),
]
