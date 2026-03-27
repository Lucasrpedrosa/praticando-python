print(''' 
      ===== Seja bem vindo(a) a verificação de contas do Banco Venturis! =====
      
      Neste programa você poderá verificar as seguintes operações:  
        - Verificar saldo;
        - Deposito direto e/ou poupança; 
        - Saque direto e/ou poupança. 
      
      ===== Exclusivo (Aposentados) ===== 
        - Saque do FGTS; 
      
      ===== Exclusivo (Juvenis) ===== 
        - Limite Reduzido de saques e depósitos (Sem acesso a poupança) 
      ''')

lista_nome = []
lista_email = []
matriz_transacoes =  []

primeiro_nome_cliente = str(input('Para começar, digite seu primeiro nome: '))

sobrenome_cliente = str(input('Digite seu sobrenome: '))



idade_cliente = int(input('Diga sua data de nascimento (Ex: dd/mm/aa): '))
while True:
    tipo_cliente = str(input(f'Olá {primeiro_nome_cliente}, informe-nos que tipo de cliente você se encaixa: \n [P] Padrão \n [A] Aposentado \n [J] Juvenil'))
    if tipo_cliente == 'P' or tipo_cliente == 'p':
        resposta = int(input('Ótimo, você já esta cadastrado como conta Padrão! Deseja realizar seu primeiro depósito? [S] Sim / [N] Não: '))
        
