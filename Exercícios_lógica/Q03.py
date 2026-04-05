'''
    Questão 03 - básico

    Realizar operação de recebe 2 notas, calcula a média. Em seguida exibe se o aluno foi aprovado, se está em recuperação ou está reprovado.
'''
import os

def clear():
    os.system('cls')



clear()
nome_aluno =str(input('Seja bem vindo(a) querido(a) aluno(a) ao calculo de sua média! Digite qual o seu nome: '))

nota_1 = float(input(f'Certo {nome_aluno}, agora digite a nota da sua 1° unidade: '))
nota_2 = float(input('Digite a nota da 2° unidade: '))
media = (nota_1 + nota_2) / 2

if media >= 7:
    print(f''' 
           ===== Parabéns {nome_aluno} você foi Aprovado! =====
            Nota 1° unidade: {nota_1}
            Nota 2° unidade: {nota_2}
            Média: {media}
            Status: Aprovado

            ''')
elif media >= 5 and media <= 6:
    print(f''' 
           ===== {nome_aluno} você está em Recuperação! =====
            Nota 1° unidade: {nota_1}
            Nota 2° unidade: {nota_2}
            Média: {media}
            Status: Recuperação

            ''')
else:
    print(f''' 
           ===== {nome_aluno} você está Reprovado =====
            Nota 1° unidade: {nota_1}
            Nota 2° unidade: {nota_2}
            Média: {media}
            Status: Reprovado

            ''')
