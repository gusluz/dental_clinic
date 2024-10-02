from django.views.generic import CreateView, ListView, DetailView
from .models import Patients
from .forms import PatientForm
from django.urls import reverse_lazy


class PatientsListView(ListView):
    template_name = 'patients/patients_list.html'
    model = Patients
    context_object_name = 'patients'


class PatientsCreateView(CreateView):
    template_name = 'patients/patients_add.html'
    model = Patients
    form_class = PatientForm
    success_url = reverse_lazy('patients:list')


class PatientsDetailView(DetailView):
    template_name = 'patients/patients_info.html'
    model = Patients
