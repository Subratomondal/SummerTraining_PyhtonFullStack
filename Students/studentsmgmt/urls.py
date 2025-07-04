from django.urls import path

from studentsmgmt import views

urlpatterns = [
    path('',views.students_list,name='students_list'),
    path('add/',views.student_create, name='students_create'),
    path('update/<int:roll_number>/',views.student_update, name='students_update'),
    path('delete/<int:roll_number>',views.student_delete, name='students_delete'),
]