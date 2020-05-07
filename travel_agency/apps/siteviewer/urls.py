from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('tours/', views.tours, name='tours'),
    path('news/', views.news, name='news'),
    path('contact/customers/', views.customer, name='customer'),
]
