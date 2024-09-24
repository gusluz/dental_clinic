from django.db import models
from django.core.exceptions import ValidationError
from patients.models import Patients
from doctors.models import Doctors
from patients.validators import validate_cpf


class Scheduling(models.Model):

    scheduling_cpf = models.CharField('CPF', max_length=14, validators=[validate_cpf])

    start = models.DateTimeField('Incio')
    end = models.DateTimeField('Término')
    
    doctor_id = models.ForeignKey(Doctors, on_delete=models.CASCADE, verbose_name='Doutor(a)')
    patient_id = models.ForeignKey(Patients, on_delete=models.CASCADE, verbose_name='Paciente', null=True, blank=True)

    observation = models.CharField('Observações', max_length=255, blank=True)


    class Meta:
        verbose_name = ("Agendamento")
        verbose_name_plural = ("Agendamentos")


    def __str__(self):
        return self.scheduling_cpf
    

    def clean(self):
        if self.end <= self.start:
            raise ValidationError('O horário de término deve ser após o horário de início.')
        

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


    # def get_absolute_url(self):
    #     return reverse("Scheduling_detail", kwargs={"pk": self.pk})


