from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_dashboard, name='room_dashboard'),
    path('room/<int:pk>/delete/', views.delete_room, name='room_delete'),
]
