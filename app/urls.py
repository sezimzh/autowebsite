from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),  
    path('cars/<int:pk>/', views.car_detail, name='car_detail'),  
     path('cars/create/', views.create_car, name='create_car'),
]