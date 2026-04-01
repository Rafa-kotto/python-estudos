import time
from ferramentas.database import carregar_usuario, buscar_cpf, salvar_usuario
from ferramentas.io_handler import limpa
from datetime import datetime


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
            extrato_bancario(pessoa, "transferencia", valor, destinatario)
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
        "tipo": tipo,
        "valor": valor,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "outro": outro,
        "id": len(pessoa["extrato"]) + 1,
    }
    pessoa["extrato"].append(registro)


def mostrar_extrato_geral(pessoa):
    limpa()
    extrato = pessoa.get("extrato", 0)
    for registro in extrato:
        print(
            f"ID : {registro['id']} | Data : {registro['data']} | Tipo : {registro['tipo']} | Valor : {registro['valor']}"
        )
    time.sleep(1)

def rendimento(valor,tempo):
    
    imposto = float(valor) * (0.01107 * float(tempo))
    simulado = valor + imposto
    return simulado

def emprestimo(valor):
    renda = 3000
    juros = 0.02
    parcelas = 3
    vparecela = []
    for parcelas in vparecela: 
        print("test")
        time.sleep(1)
        vparecela = valor * (juros *(1 + juros)**parcelas) / ((1 + juros)**parcelas- 1) 
        if vparecela < renda * 0.30:
            print(f"Possiveis parcelas{parcelas}")
            time.sleep(10)
        else :
            print("red")
            time.sleep(10)
    return vparecela



    


