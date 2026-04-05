'''
    Questão 09 - Intermediário

    Realizar operação que recebe senha e confirmação de senha até a confirmação ser aceita.
'''

import os

def clear():
    os.system('cls')

clear()
senha = str(input('Digite sua senha: '))
confirm_senha = str(input('Confirme sua senha: '))
while confirm_senha != senha:
    print('Senha incorreta! Confirme novamente...')
    confirm_senha = str(input('Confirme sua senha: '))
clear()
print('Acesso permitido!')
