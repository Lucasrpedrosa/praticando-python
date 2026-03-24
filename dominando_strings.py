nome = str(input('Digite seu nome: '))

print(f'Olá {nome.upper()} em maiúsculo!')
print(f'Olá {nome.lower()} em Minúsculo!')
print(f'Olá {nome.title()} em título!')

nome_2 = str(input('Digite outro nome: '))

print(f'Correção de margem da esquerda ---> ({nome_2.lstrip()})')
print(f'Correção de margem da direita ---> ({nome_2.rstrip()})')
print(f'Correção de margem de ambos os lados ---> ({nome_2.strip()})')

print(f'Adicionando centralização com [*] ao {nome.center(10, "*")} ')
print(f'Adicionando [.] entre o {".".join(nome_2)}')