import time
#Conta Corrente
#Saque
def saque(valor,saldo):
    if(valor<=saldo):
       saldo = saldo - valor
       print('Saque efetuado com sucesso!')
    else:
        print('Saldo insuficiente!')   

    return saldo    
#Depositar
def deposito(valor,saldo):
    saldo = saldo + valor
    print('Depósito efetuado com sucesso!')
    return saldo
#Ver saldo
def ver_saldo(saldo):
    print('O seu saldo é R$',saldo)

#Principal
saldo = 1000
print('=== Bank ESP === ')
opcao = ''
while(opcao != 'S'):
    print('Operações: 1 - Saldo, 2 - Saque, 3 - Deposito')
    print('S - Sair')
    opcao = input('Digite a operação bancária: ')
    #Leia da tela
    if(opcao =='1'):
       ver_saldo(saldo)
    elif (opcao == '2'):
       valor = float(input("Digite o valor a sacar: "))
       if (valor > 0):
          saldo = saque(valor,saldo)
          ver_saldo(saldo)
       else:
           print('Valor inválido!')
    elif (opcao == '3'):
        valor = float(input("Digite o valor a depositar: "))
        if (valor > 0):
          saldo = deposito(valor,saldo)
          ver_saldo(saldo)
        else:
           print('Valor inválido!')
    elif(opcao == 'S'): 
        print('Encerrando atendimento...')
        time.sleep(5)
    else:
        print('Operação inválida')                
              






