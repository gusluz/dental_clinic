from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teste', views.teste, name='teste'),
    path('404', views.teste404, name='teste404'),
]
