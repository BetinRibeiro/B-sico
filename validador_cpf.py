import re

def validar_cpf(cpf):
    cpf = ''.join(re.findall(r'\d', str(cpf)))

    if not cpf or len(cpf) != 11:
        return False

    antigo = [int(d) for d in cpf]

    # Gera CPF com novos dígitos verificadores e compara com CPF informado
    novo = antigo[:9]
    while len(novo) < 11:
        resto = sum([v * (len(novo) + 1 - i) for i, v in enumerate(novo)]) % 11

        digito_verificador = 0 if resto <= 1 else 11 - resto

        novo.append(digito_verificador)

    if novo == antigo:
        return True

    return False
