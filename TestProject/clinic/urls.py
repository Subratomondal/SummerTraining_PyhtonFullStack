from django.urls import path
from .views import *

urlpatterns = [
    path('', PatientListView.as_view(), name='patient_list'),
    path('add/', PatientCreateView.as_view(), name='patient_add'),
    path('<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('<int:pk>/edit/', PatientUpdateView.as_view(), name='patient_edit'),
    path('<int:pk>/delete/', PatientDeleteView.as_view(), name='patient_delete'),
]
