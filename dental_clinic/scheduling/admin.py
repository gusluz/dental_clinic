from django.contrib import admin
from scheduling.models import Scheduling


class SchedulingModelAdmin(admin.ModelAdmin):
    list_display = ('scheduling_cpf', 'start', 'doctor_id', 'patient_id')


admin.site.register(Scheduling, SchedulingModelAdmin)


# Register your models here.
