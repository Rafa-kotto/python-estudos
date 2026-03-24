import os
import time
import json
from datetime import datetime
datetime.now().strftime("%d/%m/%Y %H:%M")
os.system("clear")


def limpa():
    os.system("clear")


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

def adicionar_saldo(pessoa, pessoas, valor):
    pessoa["saldo"] = pessoa.get("saldo", 0) + float(valor)
    with open("dados.json", "w") as arquivo:
        json.dump(pessoas, arquivo, indent=4)


def retirar_saldo(pessoa, pessoas, valor):
    pessoa["saldo"] = pessoa.get("saldo", 0) - float(valor)
    with open("dados.json", "w") as arquivo:
        json.dump(pessoas, arquivo, indent=4)


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


def saldo_positivo(pessoa, valor):
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


def transferencia(pessoa, valor, pessoas):
    carregar_usuario()
    if saldo_positivo(pessoa, valor):
        cpf = int(input("Digite o cpf do destinatio: "))
        destinatario = buscar_cpf(cpf, pessoas)
        if destinatario:
            pessoa["saldo"] = pessoa.get("saldo", 0)
            pessoa["saldo"] = pessoa["saldo"] - float(valor)
            destinatario["saldo"] = destinatario["saldo"] + float(valor)
            extrato_bancario(pessoa,"transferencia",valor, destinatario )
            salvar_usuario(pessoas)
            print("deu certo")
            time.sleep(1)
        else:
            print("CPF não está cadastrado!")
            time.sleep(1)

def extrato_bancario(pessoa, tipo, valor, outro=None):
    if "extrato" not in pessoa:
        pessoa["extrato"] = []
    registro = {
        "tipo" : tipo,
        "valor" : valor,
        "data" : datetime.now().strftime("%d/%m/%Y %H:%M"),
        "outro" : outro
    }
    pessoa["extrato"].append(registro)

#def mostrar_extrato():

carregar_usuario()

def primeiro_acesso():
    os.system("clear")
    print("Bem-vindo ao nosso sistema!")
    a = input("Deseja realizar o login ou realizar o cadastro : ")
    pessoas = carregar_usuario()
    if a == "cadastro":
        os.system("clear")
        nome = input("Digite seu  nome : ")
        senha = input("Digite sua senha : ")
        nova_pessoa = {"nome": nome, "senha": senha, "saldo": 0.0}
        pessoas.append(nova_pessoa)
        salvar_usuario(pessoas)
        print("Cadastro adicionado com sucesso")
        tela_inicial(nova_pessoa, pessoas)

    elif a == "login":
        while True:
            carregar_usuario()
            if pessoas:
                u = input("Digite seu usuário : ")
                s = input("Digite sua senha : ")
                pessoa = buscar_usuario(u, pessoas)
                if pessoa and pessoa["senha"] == s:
                    tela_inicial(pessoa, pessoas)
                else:
                    print("Dados incorretos")
                    dadoerrado = input(
                        "Aperte tab para tentar novamente ou digite sair para sair"
                    )
                    os.system("clear")
                    if dadoerrado == "sair":
                        break
            else:
                print("Nenhum cadastro disponivel")
                time.sleep(1)
                primeiro_acesso()
    else:
        print("Selecione uma opção valida")
        time.sleep(0.5)
        primeiro_acesso()


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


def tela_inicial(pessoa, pessoas):
    while True:
        os.system("clear")
        print("Bem vindo ao nosso banco!")
        print("1 - verificar saldos")
        print("2 - guardar dinheiro")
        print("3 - retirar dinheiro")
        print("4 - transferir valor")
        print("5 - Alterar dados")
        print("6 - Sair")
        descisaobanco = input("O que deseja fazer : ")
        if descisaobanco == "1":
            print("a")
            os.system("clear")
            pessoa["saldo"] = pessoa.get("saldo", 0)
            print(f"O seu saldo é : {pessoa['saldo']}")
            time.sleep(2)
            
        elif descisaobanco == "2":
            limpa()
            print(f"Valor atual : {pessoa['saldo']}")
            valor = verifica_valor("Qual valor deseja adicionar ?")
            print(f"Valor de {valor} foi adicionado a sua conta!")
            extrato_bancario(pessoa, "deposito", valor)        
            adicionar_saldo(pessoa, pessoas, valor)
            

        elif descisaobanco == "3":
            limpa()
            pessoa["saldo"] = pessoa.get("saldo", 0)
            print(f"Saldo atual é : {pessoa['saldo']}")
            if pessoa["saldo"] > 0:
                retirar = verifica_valor("Digite o valor a ser retirado : ")
                limpa()
            else:
                print("Saldo insuficiente para retirar")
            senha = input("Digite sua senha para confirmar a retirada : ")
            if verifica_senha(pessoa, senha):
                print(f"Valor de R${retirar} foi retirado com sucesso!")
                extrato_bancario(pessoa,"retirada",retirar)
                retirar_saldo(pessoa, pessoas, retirar)
                time.sleep(1)
            else:
                a = 2
                while a != 0:
                    limpa()
                    print(f"Senha incorreta!, {a} tentativas restantes ")
                    senha = input("Digite a senha novamente : ")
                    if verifica_senha(pessoa, senha):
                        limpa()
                        print("Valor retirado com sucesso!")
                        time.sleep(2)
                        extrato_bancario(pessoa,"retirada",retirar)
                        retirar_saldo(pessoa, pessoas, retirar)
                        break
                    a -= 1
                print("Não ah mais tentativas restantes, voltando a tela inicial")
        elif descisaobanco == "4":
            limpa()
            valor = verifica_valor("Qual valor deseja transferir : ")
            transferencia(pessoa, valor, pessoas)

        elif descisaobanco == "5":
            trocar_dados()
            time.sleep(1)
            tela_inicial(pessoa, pessoa)
        elif descisaobanco == "6":
            break
        else:
            print("Digite uma oppção válida!")
            time.sleep(1)
            tela_inicial(pessoa, pessoas)


primeiro_acesso()
