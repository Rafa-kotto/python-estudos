import os
import time
import json
from datetime import datetime
from ferramentas.io_handler import limpa, verifica_valor, verifica_senha
from ferramentas.database import adicionar_saldo, retirar_saldo, trocar_dados
from interface.menu import primeiro_acesso
from regras_do_banco.bank_logic import extrato_bancario, transferencia, mostrar_extrato_geral

datetime.now().strftime("%d/%m/%Y %H:%M")
os.system("clear")




primeiro_acesso()
