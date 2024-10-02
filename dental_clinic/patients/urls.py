from django.urls import path, include
from .views import *


app_name = 'patients'
urlpatterns = [
    path('list', PatientsListView.as_view(), name='list'),
    path('add', PatientsCreateView.as_view(), name='add'),
    path('info/<int:pk>', PatientsDetailView.as_view(), name='info'),
    path('edit/<int:pk>', PatientsUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', PatientsDeleteView.as_view(), name='delete'),
]
