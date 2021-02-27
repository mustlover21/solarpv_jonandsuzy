from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('cyber/', views.cyber_view, name='cyber'),
    path('data/', views.data_view, name='data'),
    #path('login/', views.login, name='login'),
    path('landing/', views.landing_view, name='landing'),
    path('landing2/', views.landing2_view, name='landing2'),
    path('modules/', views.modules_view, name='modules'),
    path('password/', views.password_view, name='password'),
    path('portal/', views.portal_view, name='portal'),
    path('privacy/', views.privacy_view, name='privacy'),
    path('randt/', views.randt_view, name='randt'),
    #path('register2/', views.register2, name='register2'),
    path('registered/', views.registered_view, name='registered'),
    path('sitemap/', views.sitemap_view, name='sitemap'),
    path('systems/', views.systems_view, name='systems'),
    path('tandc/', views.tandc_view, name='tandc'),
]
