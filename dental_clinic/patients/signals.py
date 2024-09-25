from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Patients
from scheduling.models import Event


@receiver(post_save, sender=Patients)
def link_event_to_patiente(sender, instance, created, **kwargs):
    if created:
        events = Event.objects.filter(scheduling_cpf=instance.cpf)
        for event in events:
            event.patient_id = instance
            event.patient_name = instance.name
            event.save()