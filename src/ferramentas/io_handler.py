import os
import time


def limpa():
    os.system("clear")


def limpa_cpf(cpf):
    cpf_limpo = "".join(filter(str.isdigit, cpf))
    return cpf_limpo


def validar_cpf(cpf):
    cpf = limpa_cpf(cpf)
    if len(cpf) != 11:
        limpa()
        print("Cpf inválido, tente novamente")
        time.sleep(1)
        return False
    return True


def formata_cpf(cpf):
    cpf_formatado = limpa_cpf(cpf)
    cpf_formatado = f"{cpf_formatado[:3]}.{cpf_formatado[3:6]}.{cpf_formatado[6:9]}-{cpf_formatado[9:12]}"
    return cpf_formatado


def verifica_senha(pessoa, senha):
    if senha == pessoa["senha"]:
        return True
    return False


def verifica_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Digite apenas valores numéricos!")


def verifica_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Digite apenas valores numéricos!")


def veirifca_saldo_positivo(pessoa, valor):
    pessoa["saldo"] = pessoa.get("saldo")
    if pessoa["saldo"] <= 0:
        print("Saldo negativo!")
        time.sleep(1)
        return False
    elif valor > pessoa["saldo"]:
        print("Valor maior que o saldo disponivel")
        time.sleep(1)
        return False
    return True
