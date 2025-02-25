import sqlite3
conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT,
        tipopessoa TEXT 
    )
''')
conn.commit()

#Função para ler o último código
def ler_ultimo():
    cursor.execute("SELECT max(id) FROM clientes")
    resultado = cursor.fetchone()
    return resultado[0]

# Função para criar um novo cliente
def criar_cliente(nome, email,tipopessoa):
    cursor.execute("INSERT INTO clientes (nome, email,tipopessoa) VALUES (?, ?,?)", (nome, email,tipopessoa))
    return resultado[0]
    conn.commit()
    return ler_ultimo()

#Função para ler todos os clientes
def ler_clientes():
    cursor.execute("SELECT * FROM clientes")
    return cursor.fetchall()  

#Ler um id
def ler_cliente(id):
    cursor.execute("SELECT * FROM clientes where id = ?",id)
    return cursor.fetchall()  

# Função para atualizar um cliente
def atualizar_cliente(id, nome, email):
    cursor.execute("UPDATE clientes SET nome = ?, email = ? WHERE id = ?", (nome, email, id))
    conn.commit() 

# Função para deletar um cliente
def deletar_cliente(id):
    cursor.execute("DELETE FROM clientes WHERE id = ?", (id,))
    conn.commit()

#Principal

print("Cadastro do Cliente")
tipo = int(input('Digite 1 - Aluno ou 2 - Responsável: '))
if (tipo == 1 or tipo == 2):
    nome = input('Digite o nome: ')
    email = input('Digite o email: ')
    fone = input('Digite o fone: ')
    id = criar_cliente(nome,email, fone, tipo)
    print('O código do cliente é ',id)
else
    print(id)

print(ler_clientes())

conn.close()
