'''
    Questão 07 - Intermediário

    Realizar operação que receba um número inteiro do usuário e em seguida exiba a soma de 1 até o número do usuário
'''

numero = int(input('Digite um número inteiro: '))

for valor in range(1, numero + 1):
    valor += 1
print(f'A soma de todos os números de 1 a {numero} é igual a {valor}')