from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home),
    path('', views.home),
    path('customer/', views.customer),
    path('products/', views.products),
]
