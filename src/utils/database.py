import json
import os


def salvar_usuario(pessoas):
    with open("dados.json", "w") as arquivo:
        json.dump(pessoas, arquivo, indent=4)


def carregar_usuario():
    if os.path.exists("dados.json") and os.path.getsize("dados.json") > 0:
        with open("dados.json", "r") as arquivo:
            return json.load(arquivo)
    return []


def buscar_usuario(nome, lista):
    for usuario in lista:
        if usuario["nome"] == nome:
            return usuario
    return None


def buscar_cpf(cpf, lista):
    for pessoa in lista:
        if pessoa["cpf"] == cpf:
            return pessoa
    return None
