from django.urls import path
from . import views

app_name = "doctors"

urlpatterns = [
    path('', views.PatientPanelView.as_view(), name='panel'),
]
