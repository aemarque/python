import time
print("=== Escola ESP ===")
opcao = 0
while (opcao != '5'):
    print('Sou Assistente Virtual')
    print(' 1 - Cadastro da Pessoa \n 2 - Ver dados da Pessoa \n 3 - Alterar \n 4 - Excluir \n 5 - Encerrar')
    opcao = input('Por favor, digite a opção: ')
    
    if opcao == '1':
        print("Cadastro da Pessoa")
        tipo = int(input('Digite 1 - Aluno ou 2 - Professor: '))
        nome = input('Digite o nome: ')
        id = input('Digite o código da pessoa: ')
        time.sleep(5)
    elif opcao == '2':
        print("Ver dados da Pessoa")
        print('ID ',id)
        print('Nome ',nome)
        if (tipo == 1):
            print('Aluno')
        else:
           print('Professor')            
    elif opcao == '3':
        print("Alterar")
    elif opcao == '4':
        print("Volte Sempre")
    elif opcao == '5':
        print("Excluir")          
    else:
        print("Opção inválida")