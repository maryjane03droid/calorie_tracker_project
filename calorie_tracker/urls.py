from django.urls import path
from . import views

urlpatterns = [
    path('', views.food_list, name='food_list'),
    path('add/', views.add_food, name='add_food'),
    path('edit/<int:pk>/', views.edit_food, name='edit_food'),
    path('delete/<int:pk>/', views.delete_food, name='delete_food'),
    path('reset/', views.reset_foods, name='reset_foods'),
]