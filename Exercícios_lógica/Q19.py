'''
    Questão 19 - Avançado

    Gerar um número aleatório de 1 a 100 que caso o usuário erre informe se o valor é maior ou menor que o sorteado.
'''

import os, random

def clear():
    os.system('cls')

clear()
n = random.randint(1, 100)

numero = int(input('Digite um número inteiro de 1 a 100 e tente adivinhar qual o número a máquina sorteou: '))
while numero != n:
    if numero > n:
        print('Passou perto! O número selecionado é maior que o sorteado!')
        print('processando nova pergunta...')
    elif numero < n:
        print('Passou perto! O número selecionado é menor que o sorteado!')
        print('processando nova pergunta...')
    else:
        print('Valor incorreto!')
    numero = int(input('Digite um número inteiro de 1 a 100 e tente adivinhar qual o número a máquina sorteou: '))
    clear()
clear()
print('Parabéns você acertou!')