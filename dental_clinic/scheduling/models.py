from datetime import datetime
from django.db import models
from django.urls import reverse
from patients.models import Patients
from doctors.models import Doctors
from patients.validators import validate_cpf


class EventManager(models.Manager):
    """ Event manager """

    def get_all_events(self):
        events = Event.objects.filter(is_active=True, is_deleted=False)
        return events

    def get_running_events(self):
        running_events = Event.objects.filter(
            is_active=True,
            is_deleted=False,
            end_time__gte=datetime.now().date(),
        ).order_by("start_time")
        return running_events


class EventAbstract(models.Model):
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at =models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Event(EventAbstract):

    scheduling_cpf = models.CharField('CPF', max_length=14, validators=[validate_cpf])
    patient_name = models.CharField('Nome', max_length=255, default='Sem Cadastro')
    description = models.CharField('Descrição', max_length=200, blank=True)
    start_time = models.DateTimeField('Início')
    end_time = models.DateTimeField('Término')
    # doctor_id = models.ForeignKey(Doctors, on_delete=models.CASCADE, verbose_name='Doutor(a)')
    patient_id = models.ForeignKey(Patients, on_delete=models.CASCADE, verbose_name='Paciente', null=True, blank=True)

    objects = EventManager()

    class Meta:
        verbose_name = ("Agendamento")
        verbose_name_plural = ("Agendamentos")


    def __str__(self):
        return self.scheduling_cpf
    

    def get_absolute_url(self):
        return reverse("event_detail", args=(self.id,))
    




