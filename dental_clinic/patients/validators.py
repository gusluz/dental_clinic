import re
from django.core.exceptions import ValidationError


INVALIDS_CPFS = ("11111111111", "22222222222", "33333333333", "44444444444", "55555555555",
                 "66666666666", "77777777777", "88888888888", "99999999999", "00000000000")


def digit_generator(cpf, weight):
    sum_digit = 0
    for n in range(weight - 1):
        sum_digit = sum_digit + int(cpf[n]) * weight
        weight = weight - 1

    digit = 11 - sum_digit % 11
    return 0 if digit > 9 else digit


def validate_cpf(value):
    cpf = re.sub(r"[^\d]", "", value)
    if len(cpf) != 11:
        raise ValidationError('CPF deve conter 11 números', 'invalid')

    first_digit = digit_generator(cpf, weight=10)

    second_digit = digit_generator(cpf, weight=11)

    if cpf in INVALIDS_CPFS or (not cpf[-2:] == "%s%s" % (first_digit, second_digit)):
        raise ValidationError('Número de CPF inválido', 'invalid')
    # Formata o CPF
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


def format_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)
    cpf = cpf.zfill(11)
    return '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])


def validate_phone(value):
    phone = re.sub(r"[^\d]", "", value)
    if len(phone) != 11:
        raise ValidationError('Telefone deve conter 11 números', 'invalid')
