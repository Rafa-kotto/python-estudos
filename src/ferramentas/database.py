import json
import os
from ferramentas.io_handler import limpa

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "..", "data", "dados.json")

def salvar_usuario(pessoas):
    with open(DATA_PATH, "w") as arquivo:
        json.dump(pessoas, arquivo, indent=4)


def carregar_usuario():
    if os.path.exists(DATA_PATH) and os.path.getsize(DATA_PATH) > 0:
        with open(DATA_PATH, "r") as arquivo:
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


def adicionar_saldo(pessoa, pessoas, valor):
    pessoa["saldo"] = pessoa.get("saldo", 0) + float(valor)
    with open(DATA_PATH, "w") as arquivo:
        json.dump(pessoas, arquivo, indent=4)


def retirar_saldo(pessoa, pessoas, valor):
    pessoa["saldo"] = pessoa.get("saldo", 0) - float(valor)
    with open(DATA_PATH, "w") as arquivo:
        json.dump(pessoas, arquivo, indent=4)

def trocar_dados():
    os.system("clear")
    print("Para criar novo usuário digite o nome e a senha")
    nomeatual = input("Digite seu nome atual : ")
    senhaatual = input("Digite sua senha atual : ")
    pessoas = carregar_usuario()
    pessoa = buscar_usuario(nomeatual, pessoas)
    if pessoa and pessoa["senha"] == senhaatual:
        novonome = input("Novo nome: ")
        novasenha = input("Nova senha: ")
        limpa()
        pessoa["nome"] = novonome
        pessoa["senha"] = novasenha
        salvar_usuario(pessoas)
        print("Seus dados foram alterados")
        input("")
    else:
        print("Dados errados!")