from django.db import models
from patients.validators import validate_cpf, validate_phone, format_cpf
from patients.estados_choices import ESTADOS_CHOICES

class Patients(models.Model):
    SEX = (
        ('M', 'MASCULINO'),
        ('F', 'FEMININO'),
    )

    MARITAL_STATUS = (
        ('ST', 'SOLTEIRO'),
        ('CS', 'CASADO'),
        ('SP', 'SEPARADO'),
        ('DV', 'DIVORCIADO'),
        ('VV', 'VIUVO'),
    )
    #---#
    name = models.CharField('NOME', max_length=255)
    cpf = models.CharField('CPF', max_length=14, validators=[validate_cpf])
    rg_number = models.CharField('RG Nº', max_length=20, blank=True)
    organization = models.CharField('ORGÃO EXPEDIDOR', max_length=100, blank=True)
    date_birth = models.DateField('NASCIDO EM')
    sex = models.CharField('SEXO', max_length=1, choices=SEX)
    place_birth = models.CharField('NATURALIDADE', max_length=100)
    country_birth = models.CharField('NACIONALIDADE', max_length=100)
    marital_status = models.CharField('ESTADO CIVIL', max_length=2 ,choices=MARITAL_STATUS)
    current_job = models.CharField('PROFISSÃO', max_length=100)
    health_plan = models.CharField('PLANO DE SAÚDE', max_length=255, blank=True)
    observation = models.TextField('OBSERVAÇÕES', blank=True)
    created_at = models.DateTimeField('CRIADO EM', auto_now_add=True)
    #---#
    phone = models.CharField('TELEFONE 1', max_length=20, validators=[validate_phone])
    phone2 = models.CharField('TELEFONE 2', max_length=20, validators=[validate_phone], blank=True)
    email = models.EmailField('EMAIL', blank=True)
    #---#
    address = models.CharField('ENDEREÇO', max_length=255)
    address_number = models.CharField('NÚMERO', max_length=10)
    address_district = models.CharField('BAIRRO', max_length=255)
    address_city = models.CharField('CIDADE', max_length=255)
    address_state = models.CharField('ESTADO', max_length=2, choices=ESTADOS_CHOICES)
    address_complement = models.CharField('COMPLEMENTO', max_length=255, blank=True)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'


    def __str__(self) -> str:
        return self.name
    

    def save(self, *args, **kwargs):
        self.cpf = format_cpf(self.cpf)
        super(Patients, self).save(*args, **kwargs)
