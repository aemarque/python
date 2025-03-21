import datetime

def calcular_idade_aniversario():
    """Calcula a idade de uma pessoa e o tempo até o próximo aniversário."""

    data_nascimento_str = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    #Objeto data
    data_nascimento = datetime.datetime.strptime(data_nascimento_str, "%d/%m/%Y").date()
    #hoje
    hoje = datetime.date.today()
    #calcula a idade
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

    #calcula proximo aniversário
    proximo_aniversario = datetime.date(hoje.year, data_nascimento.month, data_nascimento.day)
    if proximo_aniversario < hoje:
        proximo_aniversario = datetime.date(hoje.year + 1, data_nascimento.month, data_nascimento.day)

    #dias para o proximo aniversário
    dias_restantes = (proximo_aniversario - hoje).days

    print(f"Sua idade é {idade} anos.")
    if (dias_restantes == 0):
        print("Parabéns hoje é seu aniversário!")
    else:
        print(f"Faltam {dias_restantes} dias para o seu próximo aniversário.")

calcular_idade_aniversario()