'''
    Questão 20 - Avançado

    Criação de dicionário com produtos e preços, podendo o cliente escolher quais procutos deseja comprar e quando irá dar o total da compra.
'''
import os

def clear():
    os.system('cls')

produtos_preços = {
    'Macarrão 1kg': {'preço': 11.90, 'numero': '1'},
    'Coca Cola 1l': {'preço': 7.50, 'numero': '2'},
    'Farinha de trigo 1kg': {'preço': 5.0, 'numero': '3'},
    'Gelatina de morango 200ml': {'preço': 6.89, 'numero': '4'},
    'Arroz 1kg': {'preço': 12.90, 'numero': '5'},
    'Feijão 1kg': {'preço': 10.30, 'numero': '6'},
    'Carne Moída 500g': {'preço': 15.50, 'numero': '7'},

}

carrinho_produto = 0
dic_produtos_selecionados = {}
while True:
    clear()
    print('''
        ===== Seja bem vindo(a) ao Atacadão! =====
        Aqui você poderá selecionar seus produtos e ir adicionando ao carrinho para sua compra final
        produtos e preços: 
            [1] Macarrão 1kg / R$ 11.90
            [2] Coca Cola 1l / R$ 7.50
            [3] Farinha de trigo 1kg / R$ 5.0
            [4] Gelatina de morango 200ml / R$ 6.89
            [5] Arroz 1kg / R$ 12.90
            [6] Feijão 1kg / R$ 10.30
            [7] Carne Moída 500g / R$ 15.50


        ''')
    selecao_produto = str(input('Digite o número do produto que deseja adicionar ao carrinho:  '))
    quantidade_produto = int(input('Digite a quantidade que deseja adicionar desse mesmo produto: '))
    
    for produto in produtos_preços.keys():
        preco_produto = produtos_preços[produto]['preço']
        if produtos_preços[produto]['numero'] == selecao_produto:
            print(f'O produto selecionado foi {produto} e seu preço é R${preco_produto}')
            print('Processando compra....')
            carrinho_produto += (preco_produto * quantidade_produto)
            dic_produtos_selecionados.update({produto: {'quantidade': quantidade_produto}})
    continuar_operacao = str(input('Deseja adicionar mais produtos para compra? [S] Sim / [N] Não '))
    if continuar_operacao == 'S' or continuar_operacao == 's':
        print('Processando...')
        continue
    elif continuar_operacao == 'N' or continuar_operacao == 'n':
        clear()
        print(' ===== Agradecemos a sua compra! =====')
        for produto_selecionado in dic_produtos_selecionados.keys():
            quantidade_selecionada = dic_produtos_selecionados[produto_selecionado]['quantidade']
            print(f'{quantidade_selecionada}x {produto_selecionado}')
        print(f'Valor total da compra: {carrinho_produto}')
    break

    
        

