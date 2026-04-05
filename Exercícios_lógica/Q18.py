'''
    Questão 18 - Avançado

    Criação e armazenamento de nomes a uma lista, em seguida exibir apenas os nomes com mais de 5 letras
'''

lista_nomes = ['Lucas', 'Guilherme', 'Eduardo', 'Vitor', 'Leonildo']

for cont in range(len(lista_nomes)):
    if len(lista_nomes[cont]) > 5:
        print(lista_nomes[cont])
    else: continue
