'''
    Questão 17

    Realizar operação que define um dicionário contendo aluno (chave), notas (valor) e indique se o aluno foi aprovado, está em recuperação ou reprovado.
'''

alunos = {
    'Lucas': {'nota': 8},
    'Vitor': {'nota': 2},
    'João': {'nota': 7},
    'Gabriel': {'nota': 9},
    'Eduardo': {'nota': 3},
    'Guilherme': {'nota': 5}
}

for nome, nota in alunos.items():
    if alunos[nome]['nota'] >= 7:
        print(f'O aluno {nome}, com nota {alunos[nome]['nota']} está Aprovado!')
    elif alunos[nome]['nota'] >= 5 and alunos[nome]['nota'] <= 6:
        print(f'O aluno {nome}, com nota {alunos[nome]['nota']} está em Recuperação!')
    else:
        print(f'O aluno {nome}, com nota {alunos[nome]['nota']} está Reprovado!')