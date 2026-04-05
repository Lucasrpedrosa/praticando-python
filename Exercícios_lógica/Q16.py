'''
    Queatão 16

    Realizar operação simples de cadastro ( até 3 pessoas )
'''

import os

def clear():
    os.system('cls')

cadastro_cliente = {}

for cont in range(1, 4):
    clear()
    print(f'''
        ===== Seja Bem vindo(a) a tela de cadastro de clientes ({cont}/3) =====
            Cadastre as seguintes informações:
            nome; 
            idade.

            ''')
    nome_cliente = str(input('Digite seu nome: '))
    idade_cliente = int(input('Digite seu idade: '))
    cadastro_cliente.update({nome_cliente: {'idade': idade_cliente}})
clear()
print(cadastro_cliente)