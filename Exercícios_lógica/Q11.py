'''
    Questão 11 

    Realizar operação onde uma lista recebe 5 números e exibe a soma e a média dos números. 
'''
lista_numeros = []

n1 = float(input('Digite um número para adicionar a lista: '))
n2 = float(input('Digite outro número para adicionar a lista: '))
n3 = float(input('Digite outro número para adicionar a lista: '))
n4 = float(input('Digite outro  número para adicionar a lista: '))
n5 = float(input('Digite outro número para adicionar a lista: '))
lista_numeros.extend([n1, n2, n3, n4, n5])
soma = 0
for valor in lista_numeros:
    soma += valor

media = (soma / len(lista_numeros))
print(f'Lista: {lista_numeros}')
print(f'A soma de todos os números da lista é {soma} e média {media}')
