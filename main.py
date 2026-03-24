import os
import time
import json
os.system('clear')


def limpa():
  os.system('clear')

def salvar_usuario(pessoas):
  with open("dados.json", "w") as arquivo:
    json.dump(pessoas, arquivo)

def carregar_usuario():
  if os.path.exists("dados.json") and os.path.getsize("dados.json") > 0:
    with open("dados.json", "r") as arquivo:
      return json.load(arquivo)
  return []

def buscar_usuario(nome,lista):
  for usuario in lista:
    if usuario["nome"] == nome:
      return usuario
  return None    


def adicionar_saldo(pessoa, pessoas, valor):
   pessoa["saldo"] =  pessoa.get("saldo", 0) + float(valor)
   with open("dados.json" , "w") as arquivo:
      json.dump(pessoas, arquivo)

def retirar_saldo(pessoa, pessoas, valor):
  pessoa["saldo"] = pessoa.get("saldo", 0) - float(valor)
  with open("dados.json" , "w") as arquivo:
    json.dump(pessoas, arquivo)

carregar_usuario()
def primeiro_acesso():
   os.system('clear')
   print("Bem-vindo ao nosso sistema!")
   a = input("Deseja realizar o login ou realizar o cadastro : ")
   pessoas = carregar_usuario()
   if a == "cadastro":
    os.system('clear')
    nome = input("Digite seu  nome : ")
    senha = input("Digite sua senha : ")
    nova_pessoa = {
       "nome" : nome,
       "senha" : senha,
       "saldo" : 0.0
    }
    pessoas.append(nova_pessoa)
    pessoa = salvar_usuario(pessoas)
    print("Cadastro adicionado com sucesso")
    tela_inicial(pessoa, pessoas)

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
                dadoerrado = input("Aperte tab para tentar novamente ou digite sair para sair")
                os.system('clear')
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
       os.system('clear')
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
    os.system('clear')
    print("Bem vindo ao nosso banco!")
    print("1 - verificar saldo")
    print("2 - guardar dinheiro") 
    print("3 - retirar dinheiro")
    print("4 - Alterar dados")
    descisaobanco = input("O que deseja fazer : ")
    if descisaobanco == "1":
       print("a")
       os.system('clear')
       pessoa["saldo"] = pessoa.get("saldo", 0)
       print(f"O seu saldo é : {pessoa("saldo")}")
       time.sleep(2)

    elif descisaobanco == "2":
       limpa()
       print("Qual valor deseja adicionar ?")
       valor = input("Valor : ")
       adicionar_saldo(pessoa, pessoas, valor)

    elif descisaobanco == "3":
       limpa()
       pessoa["saldo"] = pessoa.get("saldo", 0)
       print(f"Saldo atual é : {pessoa["saldo"]}")
       if pessoa["saldo"] > 0:
         retirar = input("Qual valor deseja retirar : ")
         retirar_saldo(pessoa, pessoas, retirar)
    elif descisaobanco == "4":
         trocar_dados()
       
    else:
      limpa()
      print("Saldo igual a R$0")
      time.sleep(1)

   

        
primeiro_acesso()      



    