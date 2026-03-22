"""
nome = 'Lucas'
idade = 17
altura = 1.76
peso_kg = 94.5

print(f'Olá! me chamo {nome}, atualmente tenho {idade} anos, {altura} metros de altura e peso {peso_kg}kg.')

print('====================================================================================')

nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura em metros: '))
peso_kg = float(input('Digite seu peso em quilogramas: '))

print(f'Seja bem vindo {nome}! vimos que você tem {idade} anos de idade, que sua altura é de {altura} metros e que pesa {peso_kg}kg.')

print('Operações aritméticas')
print('Operação de soma: 5 + 5 = ', 5 + 5)
print('Operação de subtração: 5 - 5 = ', 5 - 5)
print('Operação de multiplicação: 5 * 5 = ', 5 * 5)
print('Operação de divisão (resto float): 5 / 5 = ', 5 / 5)
print('Operação de divisão (resto inteiro): 5 // 5 = ', 5 // 5)
print('Operação de módulo: 5 % 5 = ', 5 % 5)
print('Operação de exponenciação: 5 ** 5 = ', 5 ** 5)
"""
print('Olá, Seja Bem Vindo(a) a um breve programa de calculadora de operadores aritméticos!')

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

print('Informe o número de uma das seguintes operações:')
print('[1] Soma')
print('[2] Subtração')
print('[3] Multiplicação')
print('[4] Divisão')
print('[5] Divisão (resto inteiro)')
print('[6] Potência')

operacao = str(input('Digite o número da operação desejada: '))

if operacao == '1':
    print(f'A operação escolhida foi Soma! O resultado de {n1} + {n2} = {n1+n2}')

elif operacao == '2':
    print(f'A operação escolhida foi Subtração! O resultado de  {n1} - {n2} = {n1-n2}')

elif operacao == '3':
    print(f'A operação escolhida foi Multiplicação! O resultado de {n1} * {n2} = {n1*n2}')

elif operacao == '4':
    print(f'A operação escolhida foi Divisão! O resultado de {n1} / {n2} = {n1/n2}')

elif operacao == '5':
    print(f'A operação escolhida foi Divisão (resto inteiro)! O resultado de {n1} // {n2} = {n1//n2}')

elif operacao == '6':
    print(f'A operação escolhida foi Potência! O resultado de {n1} ** {n2} = {n1**n2}')

else:
    print('Ocorreu um erro!!!')

    