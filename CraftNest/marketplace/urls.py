from django.urls import path

from marketplace import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('productlist/',views.product_list, name='product_list'),
    path('contact/',views.contact_us, name='contact_us'),
]