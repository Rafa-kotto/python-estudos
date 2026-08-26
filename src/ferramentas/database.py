import json
import os
import time
from ferramentas.io_handler import limpa
from ferramentas.io_handler import verifica_senha

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

def att_user_setings(decisao, nomeatual, senhaatual, novonome, novasenha):
    pessoas = carregar_usuario()
    pessoa = buscar_usuario(nomeatual, pessoas)
    if verifica_senha(pessoa, senhaatual):
        if decisao == "1":
            pessoa["nome"] = novonome
            pessoa["senha"] = novasenha
        elif decisao == "2":
            pessoa["nome"] = novonome
        elif decisao == "3":
            pessoa["senha"] = novasenha
        salvar_usuario(pessoas)
        print("Dados atualizados com sucesso!")
        
    else:
        print("Nome ou senha incorretos. Não foi possível atualizar os dados.")

def deleta_conta(nomeatual,senhaatual):
    pessoas = carregar_usuario()
    pessoa = buscar_usuario(nomeatual, pessoas)
    if verifica_senha(pessoa, senhaatual):
        pessoas.remove(pessoa)
        salvar_usuario(pessoas)
        print("Conta deletada com sucesso!")
    else:
        print("Nome ou senha incorretos. Não foi possível deletar a conta.")
