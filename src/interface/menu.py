from ferramentas.database import (
    carregar_usuario,
    salvar_usuario,
    limpa,
    buscar_usuario,
    adicionar_saldo,
    retirar_saldo,
    trocar_dados,
)
from ferramentas.io_handler import (
    validar_cpf,
    formata_cpf,
    verifica_valor,
    verifica_senha,
)
from regras_do_banco.bank_logic import (
    transferencia,
    extrato_bancario,
    mostrar_extrato_geral,
    rendimento,
)
import os, time


def primeiro_acesso():
    os.system("clear")
    print("Bem-vindo ao nosso sistema!")
    a = input("Deseja realizar o login ou realizar o cadastro : ")
    pessoas = carregar_usuario()
    if a == "cadastro":
        while True:
            os.system("clear")
            nome = input("Digite seu  nome : ")
            senha = input("Digite sua senha : ")
            cpf = input("Digite seu cpf : ")
            if validar_cpf(cpf):
                nova_pessoa = {
                    "nome": nome,
                    "senha": senha,
                    "saldo": 0.0,
                    "cpf": formata_cpf(cpf),
                }
                pessoas.append(nova_pessoa)
                salvar_usuario(pessoas)
                print("Cadastro adicionado com sucesso")
                tela_inicial(nova_pessoa, pessoas)
            else:
                limpa()
                print("Cpf invalido")

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


def tela_inicial(pessoa, pessoas):
    while True:
        os.system("clear")
        print("Bem vindo ao nosso banco!")
        print("1 - verificar saldos")
        print("2 - guardar dinheiro")
        print("3 - retirar dinheiro")
        print("4 - transferir valor")
        print("5 - Alterar dados")
        print("6 - mostrar extrato")
        print("7 - simular rendimento")
        print("8 - Sair")
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
                extrato_bancario(pessoa, "retirada", retirar)
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
                        extrato_bancario(pessoa, "retirada", retirar)
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
            mostrar_extrato_geral(pessoa)
        elif descisaobanco == "7":
            limpa()
            pessoa["saldo"] = pessoa.get("saldo")
            print(f"Saldo atual é {pessoa['saldo']}")
            tempo = input("Quanto tempo você quer simular em meses : ")
            resultado = rendimento(pessoa["saldo"], tempo)
            print(f"O valor será daqui {tempo} meses será de R${resultado}")
            time.sleep(2)
        elif descisaobanco == "8":
            break

        else:
            print("Digite uma oppção válida!")
            time.sleep(1)
            tela_inicial(pessoa, pessoas)
