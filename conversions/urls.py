from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('convert_long/', views.convert_long, name='convert'),
    path('convert_weight/', views.convert_weight, name='convert'),
    path('convert_temperature/', views.convert_temperature, name='convert'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
