from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Event
from patients.models import Patients


@receiver(post_save, sender=Event)
def link_patient_to_event(sender, instance, created, **kwargs):
    if created:
        try:
            patient = Patients.objects.get(cpf=instance.scheduling_cpf)
            instance.patient_id = patient
            instance.patient_name = patient.name
        except Patients.DoesNotExist:
            instance.patient_name = f"{instance.patient_name} - (Sem Cadastro)"
        instance.save()