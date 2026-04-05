'''
    Questão 06 - Intermediário

    Realizar operação de recebe um número inteiro e em seguida exibe sua tabuada completa
'''

numero = int(input('Digite um número para saber com a sua tabuada: '))

for valor in range(1,11):
    print(f'{numero} x {valor} = {numero * valor}')