'''
    Questão 15

    Realizar operação que define uma tupla de números e conta quantas vezes o número apareceu
'''

tupla = (23, 2, 7, 7, 34, 78, 2, 1, 12, 12, 23, 34)
cont = []
for valor in tupla:
    if valor not in cont:
        cont.append(valor)
        print(f'O número {valor}, apareceu {tupla.count(valor)} vez(es)!')
    else:
        continue
