from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),  
    path('cars/<int:pk>/', views.car_detail, name='car_detail'),  
    path('cars/create/', views.create_car, name='create_car'),
    path('cars/<int:pk>/edit/', views.update_car, name='update_car'),
    path('cars/<int:pk>/delete/', views.delete_car, name='delete_car'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]