from django.contrib import admin
from patients.forms import AddressForm, ContactForm
from patients.models import Address, Contact, Patients


class AddressInline(admin.StackedInline):
    model = Address
    form = AddressForm
    max_num = 1
    min_num = 1


class ContactInline(admin.StackedInline):
    model = Contact
    form = ContactForm
    max_num = 1
    min_num = 1


class PatientsModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created_at')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'
    search_fields = ('name', 'cpf',)
    inlines = [ContactInline, AddressInline]


    def phone(self, obj):
        # return Contact.phone.filter(patients=obj).first()
        return Contact.objects.filter(patient=obj).first()
    phone.short_description = 'Telefone'



admin.site.register(Patients, PatientsModelAdmin)



