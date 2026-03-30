import os

def limpa():
    os.system("clear")


def verifica_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Digite apenas valores numéricos!")
