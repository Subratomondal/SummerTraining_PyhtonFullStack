from django.urls import path

from bookmgmt import views

urlpatterns =[
    path('',views.book_list,name='book_list'),
]