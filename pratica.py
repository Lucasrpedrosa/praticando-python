import random
"""
pergunta = int(input('Diga uma operação: \n [1] Somar \n [2] Subrair \n'))

operacao = 'Soma' if pergunta == 1 else 'falha_1'


print(f'Opareção {operacao} escolhida!')


for n in range(1,11): --> Números de 1 a 10
    print(n, end=' ')

print()

for n2 in range(0, 21, 2): --> Números pares
    print(n2, end=' ')

print()

for n3 in range(1, 101): --> Soma dos números de 1 a 100
    n3 += 1
    print(n3)
print()

tabuada = int(input('Digite um número de 1 a 10 para saber qual a sua tabuada completa: '))
cont = 0
for valor in range(0, (11*tabuada), tabuada): --> Tabudade de números
    print(f'{tabuada} x {cont} = {valor}')
    cont += 1
print()

for n in range(-10, 0):    --> Sequência de -10 a -1
    print(n, end=' ')
print()

txt = input('Digite uma palavra: ')
cont = 0 
for letra in txt:           --> Contador de Letras
    cont += 1
print(f'A palavra {txt} contem {cont} letras!')


txt = input('Digite uma palavra para saber suas vogais: ')
VOGAIS = "AEIOU"

for letra in txt:
    if letra.upper() in VOGAIS:       --> Contador de Vogais
        print(letra, end=' ')

for i in list(range(1,11)):
    print(i**2, end=' ')
"""

    
n1 = random.randint(0,10)

n2 = int(input('DIgite um número de 0 a 10: '))

while n2 != n1:
    if n2 == n1:
        print('Parabéns, Você acertou!')
    elif n2 < n1 or n2 > n1:
        resp = str(input('Poxa foi quase! Deseja continuar a operação? Digite S(Sim) ou N(Não): '))
        if resp == 'S' or resp == 's':
            print('Continuando...')
        elif resp == 'N' or resp == 'n':
            break
        else: 
            print('Erro! Responda novamente')
            continue
    n2 = int(input('Tente Adivinhar novamente: '))