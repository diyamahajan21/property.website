from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('property/<int:pk>/', views.property_detail, name='property_detail'),
    path('buy/', views.buy_properties, name='buy_properties'),
    path('rent/', views.rent_properties, name='rent_properties'),
    path('sell/', views.sell_properties, name='sell_properties'),
]
