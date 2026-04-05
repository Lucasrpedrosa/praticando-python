'''
    Questão 02 - básico
    
    Realizar operação que recebe a idade do usuário, em seguida exibe se é menor de idade, adulto ou idoso
'''

nome = str(input('Olá, seja bem vindo(a), qual seu nome? : '))

idade = int(input(f'Certo {nome}, informe sua idade: '))
if idade >= 18 and idade <= 55:
    print(f'{nome} verificamos que você possui {idade} anos de idade, portanto você já é considerado um(a) adulto(a)!')
elif idade > 55:
    print(f'{nome} verificamos que você possui {idade} anos de idade, portanto você em considerado um(a) idoso(a)!')
else:
    print(f'{nome} verificamos que você possui {idade} anos de idade, portanto é menor de idade!')