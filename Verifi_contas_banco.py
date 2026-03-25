print(f' Seja bem vindo(a) a verificação de contas do Banco Venturis! \n Neste programa você poderá verificar as seguintes operações: \n - Verificar saldo; \n  - Deposito direto e/ou poupança; \n  - Saque direto e/ou poupança. \n ===== Exclusivo (Aposentados) ===== \n  - Saque do FGTS; \n ===== Exclusivo (Juvenis) ===== \n  - Limite Reduzido de saques e depósitos (Sem acesso a poupança) ')

primeiro_nome_cliente = str(input('Para começar, digite seu primeiro nome: '))
sobrenome_cliente = str(input('Digite seu sobrenome: '))
idade_cliente = int(input('Diga sua data de nascimento (Ex: dd/mm/aa): '))
while True:
    tipo_cliente = str(input(f'Olá {primeiro_nome_cliente}, informe-nos que tipo de cliente você se encaixa: \n [P] Padrão \n [A] Aposentado \n [J] Juvenil'))
    if tipo_cliente == 'P' or tipo_cliente == 'p':
        resposta = int(input('Ótimo, você já esta cadastrado como conta Padrão! Deseja realizar seu primeiro depósito? [S] Sim / [N] Não: '))
        
