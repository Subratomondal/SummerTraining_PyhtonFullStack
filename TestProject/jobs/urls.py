from django.urls import path
from .views import *

urlpatterns = [
    path('', JobListView.as_view(), name='job_list'),
    path('<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    path('add/', JobCreateView.as_view(), name='job_add'),
    path('<int:pk>/edit/', JobUpdateView.as_view(), name='job_edit'),
    path('<int:pk>/delete/', JobDeleteView.as_view(), name='job_delete'),
]
