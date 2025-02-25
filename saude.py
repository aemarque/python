#Saude em dia - Verifica se a pressão arterial está Alta ou Normal
class Pessoa():
    #Instancia do objeto pessoa
    def __init__(self, sus, nome, idade, genero):
        self.sus = sus
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.peso = 0
        self.altura = 0
        self.pressao_min = 0
        self.pressao_max = 0

    def setPressao(self, pressaomax, pressaomin):
        self.pressao_max = pressaomax
        self.pressao_min = pressaomin

    def checkPressao(self):
        status = ""
        if (self.pressao_max >180):
            status = "Hipertensão Grave"
        elif(self.pressao_max > 139):
            status = "Hipertensão"
        elif(self.pressao_max > 129):
            status = "Alta"
        else:
            status = "Normal"
            
        return status 

#Pricipal
print('=== SAÚDE EM DIA ===')
opcao = 0
valor = 0
while(opcao != 5):
    print('=== Assistente Virtual === ')
    print('1 - Cadastro da Pessoa \n2 - Setar a pressão ')
    print('3 - Diagnóstico cardio \n4 - Consulta \n5 - Sair')
    opcao = int(input('Digite a opção desejada: '))
    if(opcao == 1):
        print('=== Dados da Pessoa === ')
        #Leitura dos dados
        sus = input("Digite o número do cartão do SUS: ")
        nome = input("Digite o nome do paciente: ")
        idade = int(input("Digite a idade do paciente: "))
        genero = input("Digite gênero do paciente(M/F/I): ")
        #Cria o objeto pessoa
        pessoa = Pessoa(sus,nome, idade,genero)
    elif(opcao == 2):    
        pressao_maxima = int(input("Digite a pressão maxima: "))
        pressao_minima = int(input("Digite a pressão mínima: "))
        #Seta a pressão arterial do paciente
        pessoa.setPressao(pressao_maxima,pressao_minima)
    elif(opcao == 3):   
        #Retorna o diagnóstico
        print("Diagnóstico: ",pessoa.checkPressao())
    elif(opcao == 4):      
        print("Consulta com o cardiologista: ")
    elif(opcao == 5):
        print('=== Cuide de sua saúde ===')
    else:
        print('Opção inválida!')       

            

