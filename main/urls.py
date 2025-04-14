from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('page1/', views.page1_view, name='page1'),
    path('page2/', views.page2_view, name='page2'),
    path('page3/', views.page3_view, name='page3'),
    path('page4/', views.page4_view, name='page4'),
]
