'''
    Questão 21 - Avançada

    Operação que define um dicionário contendo alunos e suas notas da 1° até 3° unidade, calcular a média da turma.
'''

alunos = {
    'Lucas': {'unidade_1': 8, 'unidade_2': 4, 'unidade_3': 5},
    'Vitor': {'unidade_1': 5, 'unidade_2': 8, 'unidade_3': 8},
    'João': {'unidade_1': 7, 'unidade_2': 10, 'unidade_3': 6},
    'Gabriel': {'unidade_1': 6, 'unidade_2': 3, 'unidade_3': 3},
    'Eduardo': {'unidade_1': 2, 'unidade_2': 9, 'unidade_3': 4},
    'Guilherme': {'unidade_1': 1, 'unidade_2': 10, 'unidade_3': 10}
}



for aluno in alunos.keys():
    media_aluno = (alunos[aluno]['unidade_1'] + alunos[aluno]['unidade_2'] + alunos[aluno]['unidade_3']) / 3
    alunos[aluno].setdefault('media', media_aluno)
    print(f'Média do aluno {aluno} é {media_aluno:.1f}')

media_turma = (alunos['Lucas']['media'] + alunos['Guilherme']['media'] + alunos['Vitor']['media'] + alunos['João']['media'] + alunos['Gabriel']['media'] + alunos['Eduardo']['media']) / 6

print(f'Média da turma: {media_turma:.1f}')