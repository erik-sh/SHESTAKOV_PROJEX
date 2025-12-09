from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cars/', views.cars_list, name='cars_list'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('services/', views.services, name='services'),
    path('suppliers/', views.suppliers, name='suppliers'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]