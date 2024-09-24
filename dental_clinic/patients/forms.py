from django import forms
# from patients.utils import link_scheduling_to_patient
from .models import Address, Contact, Patients


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = '__all__'

    # def save(self, commit=True):
    #     patient = super().save(commit=False)
    #     scheduling_cpf = self.cleaned_data.get('cpf')
    #     if scheduling_cpf:
    #         link_scheduling_to_patient(patient, scheduling_cpf)
    #     if commit:
    #         patient.save()
    #     return patient


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address'].required = True
        self.fields['address_number'].required = True
        self.fields['address_district'].required = True
        self.fields['address_city'].required = True
        self.fields['address_state'].required = True


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].required = True
