import time
#Funções
#Função soma
def soma(a, b):    
    return a + b

#Função subtrai
def subtrai(a, b):    
    return a - b

#Função multiplica
def multi(a, b):    
    return a * b

#Função dividi
def dividir(a, b):
    if(b!=0):    
       return a / b
    else:
        return 0
    
#Principal
print('=== Calculadora === ')
opcao = ''
while(opcao != 'S'):
    print('Operações: + : Soma, - : Subtração, *: Multiplicação, /: Divisão')
    print('S - Sair')
    opcao = input('Digite a operação da calculadora: ')
    #Leia da tela
    if(opcao !='S'):
       n1 = float(input("Digite um número: "))
       n2 = float(input("Digite outro número: "))
    
    if(opcao == '+'):
        #Chama a função de soma
        r = soma(n1,n2) 
        print('Soma de ',n1,' + ',n2,' = ',r)
        time.sleep(5)
    elif(opcao == '-'):    
        r = subtrai(n1,n2) 
        print('Subtração de ',n1,' - ',n2,' = ',r)
        time.sleep(5)
    elif(opcao == '*'):    
        r = multi(n1,n2) 
        print('Multiplicação de ',n1,' * ',n2,' = ',r)
        time.sleep(5)
    elif(opcao == '/'):    
        r = dividir(n1,n2) 
        print('Divisão de ',n1,' / ',n2,' = ',r)
        time.sleep(5)
    elif(opcao == 'S'): 
        print('Encerrando..')
        time.sleep(5)
    else:
        print('Operação inválida') 
        
        

      

