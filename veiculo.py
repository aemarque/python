#Classe Veiculo
class Veiculo():
    #Instancia do objeto veiculo
    def __init__(self, placa, ano,cor):
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.valor = 0
        self.tanque = 45
    #Métodos
    #Função que atribui valor do veiculo
    def setValor(self,valor):
        self.valor = valor

    def calcularKmLitro(self,km):
        return km/self.tanque

#Pricipal
#Leitura dos dados
placa = input("Digite a placa: ")
cor = input("Digite a cor: ")
ano = int(input("Digite o ano: "))
#Cria o objeto veiculo
carro = Veiculo(placa,ano,cor)
valor = float(input("Digite o valor: "))
#Chama o método setValor
carro.setValor(valor)
km = float(input("Digite os Km que realizou: "))
#Mostra os dados na tela
print(carro.placa)
print(carro.ano)
print(carro.cor)
print(round(carro.valor,2))
print(round(carro.calcularKmLitro(km),2),'km/litro')
