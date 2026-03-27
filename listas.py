# Lista padrão

lista_nome = ["Lucas", "Vitor", "Gabriel"]

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


