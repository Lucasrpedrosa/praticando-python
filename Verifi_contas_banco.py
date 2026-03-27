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
lista_senhas = []
matriz_transacoes =  []


cadastro_cliente = str(input('Para começar, diga-nos se você já possui cadastro no Banco Venturis? [S] Sim / [N] Não: '))
if cadastro_cliente == 'N' or cadastro_cliente == 'n':
  while True:
        
    primeiro_nome_cliente = str(input('Para começar, digite seu primeiro nome: '))
    sobrenome_cliente = str(input('Digite seu sobrenome: '))
    lista_nome.extend(f'{primeiro_nome_cliente} {sobrenome_cliente}')
        
    email_cliente = str(input('Informe-nos seu email: '))
    if '@gmail.com' not in email_cliente:
      lista_email.append(f'{email_cliente}@gmail.com')

    elif '@gmail.com' in email_cliente:
      lista_email.append(email_cliente)

    else:
      print('Email invalálido!')
      continue
      
    senha_cliente = str(input('Digite sua senha: '))
    confirm_senha_cliente = str(input('Confirme sua senha: '))
    while confirm_senha_cliente != senha_cliente:
      print('Valor inváido, digite novamente!')
    
    if confirm_senha_cliente == senha_cliente: 
      print('Senha cadastrada com sucesso!')
      lista_senhas.append(senha_cliente)