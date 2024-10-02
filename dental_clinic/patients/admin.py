from django.contrib import admin
from patients.models import Patients


class PatientsModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created_at')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'
    search_fields = ('name', 'cpf',)


admin.site.register(Patients, PatientsModelAdmin)



