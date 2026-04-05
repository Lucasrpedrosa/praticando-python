'''
    Questão 08 - Intermediário

    Realizar operação que recebe e soma números até receber o valor 0
'''

import os

def clear():
    os.system('cls')

clear()
numero = float(input('Digite um número: '))
soma = 0
while numero != 0:
    soma += numero
    numero = float(input('Digite um número: '))
clear()  
print(f'A soma total foi de {soma}')