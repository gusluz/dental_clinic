from django.db import models


class Doctors(models.Model):
    name = models.CharField('NOME', max_length=255)
    specialty = models.CharField('ESPECIALIDADE', max_length=255)
    cro = models.CharField('CRO', max_length=15)


    class Meta:
        verbose_name = 'Doutor'
        verbose_name_plural = 'Doutores'


    def __str__(self) -> str:
        return self.name
    