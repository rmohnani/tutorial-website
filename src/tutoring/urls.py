from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tutorsignup', views.tutorsignup, name='tutorsignup'),
    path('tuteesignup', views.tuteesignup, name='tuteesignup'),
]