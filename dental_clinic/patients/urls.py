from django.urls import path, include
from .views import PatientsListView, PatientsCreateView, PatientsDetailView


app_name = 'patients'
urlpatterns = [
    path('list', PatientsListView.as_view(), name='list'),
    path('add', PatientsCreateView.as_view(), name='add'),
    path('info/<pk>', PatientsDetailView.as_view(), name='info'),
]
