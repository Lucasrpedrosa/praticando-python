import random

print('Olá, Bem Vindo(a) ao teste de operadores de comparação e atribuição!')

print('O programa irá funcionar da seguinte forma: O computador ira selecionar uma número de 1 a 10, sua missão é adivinhar qual é o valor exato, mas caso não consiga acertar de primeira,  o computador ira informar e dar dicas se o valor selecionado por você é maior ou menor que o valor padrão. Em seguida pedirá para informar qual operação e qual valor vc escolherá para tentar novamente acertar o valor da máquina.')

n1 = random.randint(1,10)
n2 = int(input('Adivinhe qual número inteiro a máquina está pensando: '))
while n2 != n1:
    
    if n2 < n1:
        continua = str(input('Passou perto! Seu valor selecionado é menor que o da máquina, deseja continuar?(S/N) '))
        if continua == 'N':
            break
        elif continua == 'S':
           operacao =  str(input('Ótimo! Escolha qual operação deseja realizar: [1] Soma ou [2] Subtração: '))
           if operacao == '1':
                soma = int(input('Quanto você quer adicionar? '))
                n1 += soma
           elif  operacao == '2':
                subtracao = int(input('Quanto você quer subtrair? '))
                n1 -= subtracao
           else:
                print('Erro Operação (menor)!')
        else:
            print('Erro Continuar (menor)!')
    elif n2 > n1:
        continua = str(input('Passou perto! Seu valor selecionado é maior que o da máquina, deseja continuar?(S/N) '))
        if continua == 'N':
            break
        elif continua == 'S':
           operacao =  str(input('Ótimo! Escolha qual operação deseja realizar: [1] Soma ou [2] Subtração: '))
           if operacao == '1':
                soma = int(input('Quanto você quer adicionar? '))
                n1 += soma
           elif  operacao == '2':
                subtracao = int(input('Quanto você quer subtrair? '))
                n1 -= subtracao
           else:
                print('Erro Operação (maior)!')
        else:
            print('Erro Continuar (maior)!')
    else:
        print('Erro Geral!')
    
    n2 = int(input('Tente adivinhar novamente: '))

if n2 == n1:
        print(f'Parabéns, você acertou! o número selecionado foi {n2}') 




    