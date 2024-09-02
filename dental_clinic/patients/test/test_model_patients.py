from datetime import date
from django.core.exceptions import ValidationError
from django.test import TestCase
from patients.models import Patients

class TestModelPatients(TestCase):
    def setUp(self):
        self.obj = Patients(
            name = 'Gustavo Luz',
            cpf = '03519356147',
            date_birth = date(year=1999, month=7, day=6),
        )
    

    def test_create(self):
        self.obj.save()
        self.assertTrue(Patients.objects.exists())


    def test_validate_cpf(self):
        invalid_cpfs = [
            "11111111111",
            "00000000000",
            "12345678901",
            "abcd1234567",
        ]

        for cpf in invalid_cpfs:
            self.obj.cpf = cpf
            with self.assertRaises(ValidationError):
                self.obj.full_clean()


    def test_datebirth(self):
        self.assertIsInstance(self.obj.date_birth, date)

