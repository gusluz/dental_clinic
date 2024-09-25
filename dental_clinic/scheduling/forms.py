from django.forms import ModelForm, DateInput
from .models import Event
from django import forms

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ["scheduling_cpf", "patient_name", "description", "start_time", "end_time"]
        # datetime-local is a HTML5 input type
        widgets = {
            "scheduling_cpf": forms.CharField(
                attrs={"class": "form-control", "placeholder": "CPF do paciente"}
            ),
            "patient_name": forms.CharField(
                attrs={"class": "form-control", "placeholder": "Nome do paciente"}
            ),
            "description": forms.CharField(
                attrs={"class": "form-control", "placeholder": "Descrição da consulta",}
            ),
            "start_time": DateInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",
            ),
            "end_time": DateInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",
            ),
        }

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields["start_time"].input_formats = ("%Y-%m-%dT%H:%M",)
        self.fields["end_time"].input_formats = ("%Y-%m-%dT%H:%M",)