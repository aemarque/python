import time

print('=== PDV ===')
opcao = 0
valor = 0
while(opcao != 5):
    print('=== Assistente Virtual === ')
    print('1 - Cadastro do Produto \n2 - Emitir Nota Fiscal ')
    print('3 - Cancelar Venda \n4 – Cadastrar Pedido de Venda \n5 – Sair')
    opcao = int(input('Digite a opção desejada: '))
    if(opcao == 1):
        print('=== Dados do Produto === ')
        id = int(input('Digite o código do produto: '))
        nome = input('Digite o nome do produto: ')
        valor = float(input('Digite o preço do produto: '))
        qtde = int(input('Digite a qtde do produto em estoque: '))
    elif(opcao == 2):
        print("Nota emitida com sucesso!")
        time.sleep(5)
    elif(opcao == 3):
        print("Venda cancelada com sucesso!")
    elif(opcao == 4):
        print('=== Dados do PDV === ')
        cliente = input('Digite o nome do cliente: ')
        produto = input('Digite 1 - Café: ')
        qtde_comp = int(input('Digite a qtde do produto: '))
        valor_total = qtde_comp * valor
        print(' Valor do pedido ',valor_total)
    elif(opcao == 5):
        print('=== Volte Sempre ===')
    else:
        print('Opção inválida!')