'''
    Questão 01 - básico
    Realizar operação que pergunte um valor e retorne se é um número par ou impar
'''

n1 = int(input('Digite um número inteiro para descobrir se ele é par ou ímpar: '))
if n1 % 2 == 0:
    print(f'O número {n1} e par!')
else:
    print(f'O número {n1} e ímpar!')