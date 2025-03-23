from django.urls import path
from . import views

urlpatterns = [
    path('convert_long/', views.convert_long, name='convert'),
    path('convert_weight/', views.convert_weight, name='convert'),
    path('convert_temperature/', views.convert_temperature, name='convert'),
]
