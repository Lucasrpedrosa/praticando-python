import os

def clear():
  os.system('cls')
    
clear()
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
lista_id = []



cadastro_cliente = str(input('Para começar, diga-nos se você já possui cadastro no Banco Venturis? [S] Sim / [N] Não: '))
if cadastro_cliente == 'N' or cadastro_cliente == 'n':
  clear()
  while True:
        
    primeiro_nome_cliente = str(input('Para começar, digite seu primeiro nome: '))
    sobrenome_cliente = str(input('Digite seu sobrenome: '))  
    email_cliente = str(input('Informe-nos seu email: '))
    if '@gmail.com' not in email_cliente:
      email_cliente = (f'{email_cliente}@gmail.com')
      
      
    senha_cliente = str(input('Digite sua senha: '))
    while True:
      confirm_senha_cliente = str(input('Confirme sua senha: '))
      if confirm_senha_cliente == senha_cliente: 
        print('Senha cadastrada com sucesso!')
        break
      else:
        print('Valor inválido! Confirme a senha novamente...')
        continue

    if 1 not in lista_id:
      id_cliente = 1
    else:
      id_cliente = (len(lista_id) + 1)
    clear()  
    print(f'''
        ===== Cadastro concluído =====
        
        Parabéns! Agora você faz parte da equipe Venturis :)
          Aqui estão seus dados:
          Nome: {primeiro_nome_cliente} {sobrenome_cliente}
          email: {email_cliente}
          senha: {senha_cliente}
          
        ''')
    
    confirm_cadastro = str(input('Deseja confirmar as informações de cadastro? [S] Sim / [N] Não: '))
    if confirm_cadastro == 'S' or confirm_cadastro == 's':
      print('Cadastro salvo com sucesso!')
      lista_nome.append(f'{primeiro_nome_cliente} {sobrenome_cliente}')
      lista_email.append(email_cliente)
      lista_senhas.append(senha_cliente)
      lista_id.append(id_cliente)
      break
    elif confirm_cadastro == 'N' or confirm_cadastro == 'n':
      novo_cadastro = str(input('Deseja sair do programa? \n [S] Sim, desejo sair / [N] Não, desejo realizar novo cadastro: '))
      if novo_cadastro == 'S' or novo_cadastro == 's':
        print('Saindo da área de cadastro...')
        break
      elif novo_cadastro == 'N' or novo_cadastro == 'n':
        print('Processando novo cadastro...')
        continue
    break
      
     
      