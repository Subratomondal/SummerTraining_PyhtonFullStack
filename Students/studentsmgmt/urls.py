from django.urls import path

from studentsmgmt import views

urlpatterns = [
    path('',views.students_list,name='students_list'),
    path('add/',views.student_create, name='students_create')
]