'''
    Questão 12

    Realizar operação que define uma lista de número e que exiba apenas os números pares
'''

lista_numeros = [34, 56, 76, 12, 77, 33, 87, 98]
lista_numeros_pares = [pares for pares in lista_numeros if pares % 2 == 0 ]

print(f' Lista de número: {lista_numeros}')
print(f' Lista de números pares: {lista_numeros_pares}')