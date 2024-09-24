# Generated by Django 4.2.15 on 2024-09-10 14:29

from django.db import migrations, models
import django.db.models.deletion
import patients.validators


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("doctors", "0002_alter_doctors_options"),
        ("patients", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Scheduling",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "scheduling_cpf",
                    models.CharField(
                        max_length=14,
                        validators=[patients.validators.validate_cpf],
                        verbose_name="CPF",
                    ),
                ),
                ("start", models.DateTimeField(verbose_name="Incio")),
                ("end", models.DateTimeField(verbose_name="Término")),
                (
                    "observation",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Observações"
                    ),
                ),
                (
                    "doctor_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="doctors.doctors",
                        verbose_name="Doutor(a)",
                    ),
                ),
                (
                    "patient_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="patients.patients",
                        verbose_name="Paciente",
                    ),
                ),
            ],
            options={
                "verbose_name": "Agendamento",
                "verbose_name_plural": "Agendamentos",
            },
        ),
    ]
