from django.urls import path
from .views import *

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('add/', CourseCreateView.as_view(), name='course_add'),
    path('<int:pk>/edit/', CourseUpdateView.as_view(), name='course_edit'),
    path('<int:pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),
]
