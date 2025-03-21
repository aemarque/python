import datetime
hoje = datetime.datetime.now()
#Escreve a data e hora de hoje 
print('Hoje é',hoje.strftime("%d/%m/%Y %H:%M"))

#Mostra a data criada
data = datetime.datetime(2025,12,25)
print('Hoje é',hoje.strftime("%d/%m/%Y"))

#Diferença entre datas
diferenca = data - hoje
print(f"Faltam: {diferenca.days} dias para o Natal!")
