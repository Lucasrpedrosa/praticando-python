nome = 'lUcAs'

print(f'Olá {nome.upper()} em maiúsculo!')
print(f'Olá {nome.lower()} em Minúsculo!')
print(f'Olá {nome.title()} em título!')

nome_2 = '  Lucas   '

print(f'Correção de margem da esquerda ---> ({nome_2.lstrip()})')
print(f'Correção de margem da direita ---> ({nome_2.rstrip()})')
print(f'Correção de margem de ambos os lados ---> ({nome_2.strip()})')

print(f'Adicionando centralização com [*] ao {nome.center(10, "*")} ')
print(f'Adicionando [.] entre o {".".join(nome_2)}')

# Adicionando definições de formatação de strings úteis (.format())

nome_3 = 'Lucas'
idade = 18
profissao = 'DevOps Engineer'

print('Olá meu nome é {2}, tenho {0} de idade e atuo como {1} no Banco Santander'.format(idade, profissao, nome_3))

# Utilizando um dicionário (dic = {""})

dados = {"nome" : "Lucas", "idade" : 18}

print('Nome: {nome} \nIdade: {idade}'.format(**dados))


# Fatiamento de string

n = "Lucas Ribeiro Pedrosa"

print(n[0])
print(n[:9])
print(n[10:])
print(n[10:16])
print(n[10:16:2])
print(n[:])
print(n[::-1])

