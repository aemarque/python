import sqlite3
import time

#Criação da base de dados
conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

#Criação da tabela clientes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT,
        fone TEXT,
        tipo int 
    )
''')

#Criação da tabela boletim
cursor.execute('''
    CREATE TABLE IF NOT EXISTS boletim (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aluno INTEGER,
        nota1 REAL,
        nota2 REAL,
        frequencia INTEGER,
        media REAL,
        conceito TEXT
               
    )
''')
conn.commit()

#Função para ler o último código
def ler_ultimo():
    cursor.execute("SELECT max(id) FROM clientes")
    resultado = cursor.fetchone()
    return resultado[0]

# Função para criar um novo cliente
def criar_cliente(nome, email,fone, tipo):
    cursor.execute("INSERT INTO clientes (nome, email,fone, tipo) VALUES (?, ?, ?, ?)", (nome, email,fone, tipo))
    conn.commit()
    return ler_ultimo()

#Função para ler todos os clientes
def ler_clientes():
    cursor.execute("SELECT * FROM clientes ")
    return cursor.fetchall()  

#Ler um id
def ler_cliente(id):    
    cursor.execute("SELECT * FROM clientes WHERE id = ?",(id))
    return cursor.fetchall()  

# Função para atualizar um cliente
def atualizar_cliente(id, nome, email, fone):
    cursor.execute("UPDATE clientes SET nome = ?, email = ?, fone = ? WHERE id = ?", (nome, email,fone, id))
    conn.commit() 

# Função para excluir um cliente
def excluir_cliente(id):
    cursor.execute("DELETE FROM clientes WHERE id = ?", (id))
    conn.commit()

#Criar boletim
def inserir_boletim(aluno, nota1, nota2, frequencia, media, conceito):
    cursor.execute(" INSERT INTO boletim (aluno, nota1, nota2, frequencia, media, conceito) VALUES (?, ?, ?, ?, ?, ?)", (aluno, nota1, nota2, frequencia, media,conceito))
    conn.commit()

#Função para ler os dados do boletim
def ler_boletim():
    cursor.execute("SELECT * FROM boletim ")
    return cursor.fetchall()  

#Principal
print("=== Escola InnovaEdu ===")
opcao = 0
while (opcao != '9'):
    print('\nSou Assistente Virtual InovvaEdu. Em que posso ajudar hoje?')
    print(' 1 - Cadastro do Cliente \n 2 - Ver dados do Cliente \n 3 - Alterar \n 4 - Excluir \n 5 - Boletim \n 9 - Encerrar')
    opcao = input('Por favor, digite apenas o número da operação desejada: ')
    if opcao == '1':
        print("=== Cadastro do Cliente ===")
        tipo = int(input('Digite 1 - Aluno ou 2 - Responsável: '))
        if (tipo == 1 or tipo == 2):
             nome = input('Digite o nome: ')
             email = input('Digite o email: ')
             fone = input('Digite o fone: ')
             id = criar_cliente(nome,email, fone, tipo)
             print('O código do cliente é ',id)            
        else:
            print('Tipo inválido!')
        time.sleep(2)  
    elif opcao == '2':
        print("Ver dados de um cliente")
        id = input('Digite o código do cliente: ')
        dados_cliente = ler_cliente(id)
        if len(dados_cliente) != 0:
           print(dados_cliente)
        else:
           print("Cliente não encontrado!")
        time.sleep(2) 
    elif opcao == '3':
        print("=== Alterar Cliente ===")
        id = input('Digite o código do cliente: ')
        nome = input('Digite o nome: ')
        email = input('Digite o email: ')
        fone = input('Digite o fone: ')
        atualizar_cliente(id, nome, email,fone)
        print("Cliente atualizado com sucesso!")
        time.sleep(2) 
    elif opcao == '4':
        print("=== Excluir Cliente === ")        
        id = input('Digite o código do cliente: ')
        excluir_cliente(id)
        print(ler_cliente(id))
        print("Cliente excluído com sucesso!")
        time.sleep(2) 
    elif opcao == '5':
        print("=== Boletim === ") 
        id = input('Digite o código do aluno: ')
        #Ler duas notas da tela
        n1 = float(input('Digite a nota 1: '))
        n2 = float(input('Digite a nota 2: '))
        freq = float(input('A frequencia do aluno: '))
        #Calcular a média
        media = (n1+n2) / 2
        #Comando condicional - iguais
        if (media >= 7):
            conceito = 'Aprovado'
            print('Aprovado! Média = ',round(media,1))
        else:
            conceito = 'Reprovado'
            print('Reprovado! Média = ',round(media,1))
        
        #Inserir o boletim do aluno
        inserir_boletim(id,n1, n2, freq,media,conceito)
        print('Boletim inserido com sucesso!')
        print(ler_boletim())
        time.sleep(2) 
    elif opcao == '9':
        print("Encerrando!") 
        time.sleep(2)          
    else:
        print("Opção inválida. Tente novamente")


#fechar o banco de dados
conn.close()
