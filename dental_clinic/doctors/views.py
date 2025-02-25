from django.shortcuts import render
from django.views import generic


class PatientPanelView(generic.TemplateView):
    template_name = "doctors/patient_panel.html"
