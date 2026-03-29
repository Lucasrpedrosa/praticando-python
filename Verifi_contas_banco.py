import os

def clear():
  os.system('cls')

while True:   
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

  lista_nome = ["Lucas"]
  lista_email = ["lucasrpedrosa25@gmail.com"]
  lista_senhas = ["lucas250380"]
  lista_id = [0]



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
          id de usuário: {id_cliente}
          
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
      continue
  elif cadastro_cliente == 'S' or cadastro_cliente == 's':
    clear()
    print('Realizando processo de login...')
    sair_login = "S"
    while sair_login != 'N' or sair_login != 'n':

      login_email_cliente = str(input('Digite seu email: '))
      if '@gmail.com' not in login_email_cliente:
        login_email_cliente = (f'{login_email_cliente}@gmail.com')
      
      login_senha_cliente = str(input('Digite sua senha: '))
      
      if login_email_cliente not in lista_email or login_senha_cliente not in lista_senhas:
        print('Email ou senha inválidos! Digite novamente...')
        continue
      
      if lista_email.index(login_email_cliente) != lista_senhas.index(login_senha_cliente):
        print('Email e senha não compativeis! Realize o login novamente...')
        continue
      else:
        clear()
        print(f'''
          ===== Seja Bem Vindo(a) =====

              Aqui estão as informações da sua conta:
              Nome completo: {lista_nome[lista_email.index(login_email_cliente)]}
              Email: {lista_email[lista_email.index(login_email_cliente)]}
              

              ''')
        sair_login = str(input('Deseja sair do programa? \n [S] Sim, desejo sair / [N] Não, desejo realizar novo login: ')) 
        if sair_login == 'S' or sair_login == 's':
          clear()
          print('''
            ===== Obrigado pelo seu tempo! =====   

            Criador: Lucas Ribeiro 

                ''')
          break
        elif sair_login == 'N' or sair_login == 'n':
          print('Processando tela de menu princial...')
          continue
        else:
          print('Valor inválido!')
          continue
    
   

  
      
     
      