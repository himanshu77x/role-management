# roles/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.role_list, name='role_list'),
    path('create/', views.create_role, name='create_role'),
    path('update/<int:pk>/', views.update_role, name='update_role'),
    path('delete/<int:pk>/', views.delete_role, name='delete_role'),
]
