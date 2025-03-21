class PacoteViagem:
    """Classe que representa um pacote de viagem."""

    def __init__(self, destino, valor, descricao, cliente):
        self.destino = destino
        self.valor = valor
        self.descricao = descricao
        self.cliente = cliente
    
    def calcular_valor_mensal(self):
        valor_mensal = 0
        if self.valor > 0:
            valor_mensal = self.valor/12
        return valor_mensal    


#Principal
while opcao != 9:
    print("\nTurismo")
    print("1. Comprar pacote de viagem")
    print("2. Calcular o valor mensal")
    print("3. Listar todos os pacotes de viagem")
    print("9. Sair")
    opcao = int(input('Digite a opção: '))


cliente = input("Digite o nome do cliente: ")
destino = input("Digite o destino do pacote: Paris/Roma")
valor = float(input("Digite o preço total do pacote: "))
descricao = input("Digite a descrição do pacote: ")
#Criação do pacote
if (valor > 0): 
    paris = PacoteViagem(destino, valor, descricao, cliente)