from django.contrib import admin
from scheduling.models import Event


class EventModelAdmin(admin.ModelAdmin):
    list_display = ('scheduling_cpf', 'patient_name', 'start_time', 'end_time', 'patient_id')


admin.site.register(Event, EventModelAdmin)


# Register your models here.
