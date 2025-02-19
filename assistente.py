# Online Python - IDE, Editor, Compiler, Interpreter
#Exemplo de switch-case com if
import time
opcao = 0
while (opcao != '4'):
    print('Sou Assistente Virtual')
    print(' 1 - Suporte \n 2 - Comercial \n 3 - Financeiro \n 4 - Encerrar atendimento')
    opcao = input('Por favor, digite a opção')
    
    if opcao == '1':
        print("Atendimento Suporte")
        time.sleep(5)
    elif opcao == '2':
        print("Atendimento Comercial")
    elif opcao == '3':
        print("Atendimento Financeiro")
    elif opcao == '4':
        print("Agradecemos o contato!")    
    else:
        print("Opção inválida")
