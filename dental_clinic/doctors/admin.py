from django.contrib import admin
from doctors.models import Doctors


class DoctorsModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'cro')


admin.site.register(Doctors, DoctorsModelAdmin)
