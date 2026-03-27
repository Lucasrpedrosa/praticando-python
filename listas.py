# Lista padrão

lista_nome = ["Lucas", "Vitor", "Gabriel", "Lucas"]

# Lista vazia

lista = []

# Lista de caracteres

m = list("python")

# Lista utilizando range

n = list(range(10))

# Chamando os valores 

lista_nome[0]   # --> Retorna o primeiro objeto da lista
lista_nome[-1]  # --> Retorna o último objeto da lista

# matriz

matriz = [
    [1, "b", 4],
    [78, "Lucas", 2008],
    [58, 25, "python"]
]

matriz[0]   # Imprime a primeira linha ([1, "b", 4])
matriz[0][0]    # Imprime o primeiro valor da primeira linha (1)
matriz[0][-1]   # Imprime o último valor da primeira linha (4)
matriz[-1][-1]  # Imprime o último valor da última linha ("pyhton")

# Fatiamento da lista

b = ["P", "y", "t", "h", "o", "n"] 

b[2:] # ["t", "h", "o", "n"]
b[:2] # ["P", "y"]
b[1:3] # ["y", "t"]
b[0:3:2] # ["P", "t"]
b[::] # ["P", "y", "t", "h", "o", "n"]
b[::-1] # ["n", "o", "h", "t", "y", "P"]

# Para ler a lista utilizando o for 

carros = ["Sandero", "HB20", "UP"]

for carro in carros:
    print(carro)

# Utilizando o for + enumerate

for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')

# Compresão de lista

    valores = [1, 60, 40, 23, 56, 7, 4]
    valor_impar = []

    for valor in valores:
        if valor % 2 != 0:
            valor_impar.append(valor)
    
    # Forma reduzida

    valores = [1, 60, 40, 23, 56, 7, 4]
    valor_impar = [ valor for valor in valores if valor % 2 != 0]

    # Mais exemplos

    valores = [1, 60, 40, 23, 56, 7, 4]
    quadrado = []

    for valor in valores:
        quadrado.append(valor ** 2)

    # Exemplo reduzido

    quadrado = [valor ** 2 for valor in valores]


    # Métodos para listas

    #.append() -  adiciona objetos a lista

    lista = []

    lista.append(1)
    lista.append("Python")
    lista.append([40, 30, 20])

    print(lista)  # [1, "Python", [40, 30, 20]]
    
    # .clear() - limpa a lista
    lista.clear()
    print(lista) # []

    # .copy() - copia a lista
    lista_nome_copy = lista_nome.copy()
    print(lista_nome)   # ["Lucas", "Vitor", "Gabriel", "Lucas"]
    print(lista_nome_copy) # ["Lucas", "Vitor", "Gabriel", "Lucas"]

    # .count() - Conta quantos objetos X tem na lista

    lista_nome.count("Vitor") # 1
    lista_nome.count("Lucas") # 2

    # .extend - Adiciona mais de um objeto de uma vez a lista

    lista.extend([1, "LUCAS", 89, 100])
    print(lista) # [1, "LUCAS", 89, 100]

    # .index() - Exibe a primeira posição em que o objeto está 

    lista_nome.index("Lucas") # 0
    lista_nome.index("Vitor") # 1

    # .pop() - Remove objetos da lista pelo indice, caso não especifique remove o último adicionado

    lista.pop() # 100
    lista.pop(0) # 1

    # .remove() - Remove o objeto da lista

    lista.remove("LUCAS")
    print(lista) # [89]

    # .reverse() - Inverte a ordem da lista

    lista_a = ["lucas", "java", "oi"]
    lista_a.reverse()
    print(lista_a)  # ["oi", "java", "lucas"]

    # len - Exibe quantos objetos tem na lista

    print(len(lista_a)) # 3

    #.sort() - ordena a lista

    linguagens = ["python", "js", "c", "java", "csharp"]
    linguagens.sort()  # ["c", "csharp", "java", "js", "python"] - Ordem alfabetica
    print(linguagens)

    linguagens = ["python", "js", "c", "java", "csharp"]
    linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"] - Inverte a ordem
    print(linguagens)

    linguagens = ["python", "js", "c", "java", "csharp"]
    linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"] - Ordem Crescente
    print(linguagens)

    linguagens = ["python", "js", "c", "java", "csharp"]
    linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"] - Ordem decrescente
    print(linguagens)


