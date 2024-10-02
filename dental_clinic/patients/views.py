from django.views import generic
from .models import Patients
from .forms import PatientForm
from django.urls import reverse_lazy
from django.http import JsonResponse


class PatientsListView(generic.ListView):
    template_name = 'patients/patients_list.html'
    model = Patients
    context_object_name = 'patients'


class PatientsCreateView(generic.CreateView):
    template_name = 'patients/patients_add.html'
    model = Patients
    form_class = PatientForm
    success_url = reverse_lazy('patients:list')


class PatientsDetailView(generic.DetailView):
    template_name = 'patients/patients_info.html'
    model = Patients
    context_object_name = 'patient'


class PatientsUpdateView(generic.UpdateView):
    template_name = 'patients/patients_edit.html'
    model = Patients
    fields = '__all__'
    context_object_name = 'patient'
    success_url = reverse_lazy('patients:list')


class PatientsDeleteView(generic.DeleteView):
    model = Patients
    success_url = reverse_lazy('patients:list')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        if request.is_ajax():
            return JsonResponse({'redirect_url': self.success_url})
        return response