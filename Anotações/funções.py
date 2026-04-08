# Declarando funções

def mensagem():
    print('Diga aí')

def mensagem_2(nome):
    print(f'Diga aí {nome}')

def mensagem_3(nome='Lucas'):
    print(f'Diga aí {nome}')

mensagem() # 'Diga aí'
mensagem_2(nome='Vitor') # 'Diga aí {Vitor}}'
mensagem_3() # 'Diga aí {Lucas}'
mensagem_3(nome='Leonildo') # 'Diga aí {Leonildo}'


# Utilizando o return

def soma_num(numeros):
    return sum(numeros)

def antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

soma_num([10, 20, 30]) # 60
antecessor_sucessor(40) # (39, 41)


# Argumentos nomeados
dicionario = {'nome': 'Lucas', 'idade': 18, 'id':6498, 'CEP': 50670-130}
def dados_cliente(nome, idade, id, CEP):
    print(f'Cliente cadastrado como {nome}/{idade}/{id}/{CEP}')

dados_cliente('Lucas', 18, 6498, 50670-130)
dados_cliente(nome='Lucas', idade=18, id=6498, CEP=50670-130)
dados_cliente(**{'nome': 'Lucas', 'idade': 18, 'id':6498, 'CEP': 50670-130})
dados_cliente(**dicionario)
# Em todos os casos a resposta será a mesma, porém nomear os documentos é importante para evitar possíveis erros no código

# Utilizando *args(listas) e **kwargs(dicionários)
def cliente_biografia(data, *conteudo, **referencias):
    texto = '\n'.join(conteudo)
    dados = '\n'.join([f'{chave.title()}: {valor}' for chave, valor in referencias.items()])
    exibe = f'{data}\n\n{texto}\n\n{dados}'
    print(exibe)

cliente_biografia( '07/04/2026', 'Olá meu nome é Lucas tenho 10 anos e gosto muito de carros', autor= 'lucas ribeiro',
        ano=89
)


# Parâmetros por posição(/) e nomeado(*)

def carro(marca, modelo, placa, /, motor, capo_carro, pneu ):
    print(marca, modelo, placa, motor, capo_carro, pneu)
carro('Fiat', 'Uno', 'A4G-89HT', motor = '2.0', capo_carro = 'none', pneu='modo')
# carro(marca='Fiat',modelo= 'Uno', placa= 'A4G-89HT', motor = '2.0', capo_carro = 'none', pneu='modo') exemplo da inválido pois apenas as variáveis que estão antes de / são por posição, não aceitando a nomeação

def carro_2(*,marca, modelo, placa, motor, capo_carro, pneu):
    print(marca, modelo, placa, motor, capo_carro, pneu)

carro_2(marca='Fiat',modelo= 'Uno', placa= 'A4G-89HT', motor = '2.0', capo_carro = 'none', pneu='modo')
 # carro_2('Fiat', 'Uno', 'A4G-89HT', motor = '2.0', capo_carro = 'none', pneu='modo')  exemplo da inválido pois as variáveis que estão depois do * só recebem nomeação


def carro_3(marca, modelo, placa, /, *, motor, capo_carro, pneu):
    print(marca, modelo, placa, motor, capo_carro, pneu)

carro_3('Fiat', 'Uno', 'A4G-89HT', motor = '2.0', capo_carro = 'none', pneu='modo') 


# Objetos de primeira classe

def somar(n1, n2):
    return n1 + n2

def exibir_resultado(n1, n2, resp):
    resposta = resp(n1, n2)
    print(f'Sua resposta é {resposta}')

exibir_resultado(20, 30, somar)

# Escopo Local e global - Para chamar variáveis que estão fora da função ( Não é recomendado utilizar o global )
nome = "Lucas"
def cliente(idade):
    global nome
    print(f'olá {nome}, você tem {idade} anos')

cliente(18)