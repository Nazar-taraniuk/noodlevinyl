from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_vinyl_order, name='create_vinyl_order'),
    path('my-orders/', views.my_orders, name='my_orders'),
]
