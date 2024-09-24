# from patients.models import Patients
# from scheduling.models import Scheduling

# #aparentemente nao esta funcionando
# def link_scheduling_to_patient(patient, scheduling_cpf):
#     try:
#         appointment = Scheduling.objects.get(scheduling_cpf=scheduling_cpf)
#         appointment.patient = patient
#         appointment.save()
#         # Enviar notificação ao paciente informando a vinculação
#     except Scheduling.DoesNotExist:
#         pass