from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('customers/', views.customers, name='customers'),
    path('customer/new', views.create_customer, name='create-customer'),
    path('customer/delete/<int:pk>/', views.delete_customer, name='delete-customer'),
]