# SITUAÇÃO PROBLEMA: CADASTRO DE CLIENTES EM UM COMÉRCIO DE VAREJO

# A EMPRESA "XYZ COMÉRCIO" TEM DIFICULDADES EM CONTROLAR O

# CADASTRO DE SEUS CLIENTES. ATUALMENTE, O ARQUIVO COM OS DADOS
# DOS CLIENTES ESTÁ DESORGANIZADO, E A EQUIPE DE VENDAS TEM

# ENCONTRADO DIFICULDADES EM ENCONTRAR INFORMAÇÕES RÁPIDO. A

# EMPRESA PRECISA DE UM SISTEMA QUE PERMITA O CADASTRO DE NOVOS

# CLIENTES, A CONSULTA DE CLIENTES JÁ CADASTRADOS E A EDIÇÃO OU
# EXCLUSÃO DE DADOS.

# Solução proposta: Criar um sistema que permita o cadastro de novos clientes

# com informações como nome, e-mail, telefone e endereço. Além disso, o

# sistema permitirá a consulta, edição e exclusão dos dados dos clientes
# através de uma interface gráfica simples.


# Requisitos  tkinter  -  interface gráfica
# Sqlite3 -  Bancos de dados 
# TTk -  Submódulo do tkinter 
# MessageBox  -  biblioteca que cria uma caixa de dialogo
# Python Puro
import tkinter as tk
from tkinter import messagebox
import sqlite3

# Função para criar o banco de dados e a tabela de clientes
def criar_banco():
    conn = sqlite3.connect('clientes.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            email TEXT,
            telefone TEXT,
            endereco TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Função para adicionar um novo cliente
def adicionar_cliente():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    endereco = entry_endereco.get()

    if nome and email and telefone and endereco:
        conn = sqlite3.connect('clientes.db')
        c = conn.cursor()
        c.execute('''
            INSERT INTO clientes (nome, email, telefone, endereco)
            VALUES (?, ?, ?, ?)
        ''', (nome, email, telefone, endereco))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        limpar_campos()
        mostrar_clientes()
    else:
        messagebox.showwarning("Campos vazios", "Preencha todos os campos!")

# Função para exibir todos os clientes na lista
def mostrar_clientes():
    lista_clientes.delete(0, tk.END)
    conn = sqlite3.connect('clientes.db')
    c = conn.cursor()
    c.execute('SELECT * FROM clientes')
    clientes = c.fetchall()
    for cliente in clientes:
        lista_clientes.insert(tk.END, f"ID: {cliente[0]} - Nome: {cliente[1]} - E-mail: {cliente[2]}")
    conn.close()

# Função para editar um cliente
def editar_cliente():
    selected = lista_clientes.curselection()
    if selected:
        cliente_id = lista_clientes.get(selected[0]).split(" - ")[0].split(":")[1].strip()
        novo_nome = entry_nome.get()
        novo_email = entry_email.get()
        novo_telefone = entry_telefone.get()
        novo_endereco = entry_endereco.get()
        
        if novo_nome and novo_email and novo_telefone and novo_endereco:
            conn = sqlite3.connect('clientes.db')
            c = conn.cursor()
            c.execute('''
                UPDATE clientes
                SET nome = ?, email = ?, telefone = ?, endereco = ?
                WHERE id = ?
            ''', (novo_nome, novo_email, novo_telefone, novo_endereco, cliente_id))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")
            mostrar_clientes()
        else:
            messagebox.showwarning("Campos vazios", "Preencha todos os campos!")
    else:
        messagebox.showwarning("Seleção inválida", "Selecione um cliente para editar!")

# Função para excluir um cliente
def excluir_cliente():
    selected = lista_clientes.curselection()
    if selected:
        cliente_id = lista_clientes.get(selected[0]).split(" - ")[0].split(":")[1].strip()
        conn = sqlite3.connect('clientes.db')
        c = conn.cursor()
        c.execute('DELETE FROM clientes WHERE id = ?', (cliente_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Cliente excluído com sucesso!")
        mostrar_clientes()
    else:
        messagebox.showwarning("Seleção inválida", "Selecione um cliente para excluir!")

# Função para limpar os campos
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)

# Criar o banco de dados ao iniciar
criar_banco()

# Interface gráfica
root = tk.Tk()
root.title("Cadastro de Clientes")

# Labels e Entrys
tk.Label(root, text="Nome:").grid(row=0, column=0, padx=10, pady=5)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="E-mail:").grid(row=1, column=0, padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Telefone:").grid(row=2, column=0, padx=10, pady=5)
entry_telefone = tk.Entry(root)
entry_telefone.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Endereço:").grid(row=3, column=0, padx=10, pady=5)
entry_endereco = tk.Entry(root)
entry_endereco.grid(row=3, column=1, padx=10, pady=5)

# Botões
tk.Button(root, text="Cadastrar Cliente", command=adicionar_cliente).grid(row=4, column=0, padx=10, pady=10)
tk.Button(root, text="Editar Cliente", command=editar_cliente).grid(row=4, column=1, padx=10, pady=10)
tk.Button(root, text="Excluir Cliente", command=excluir_cliente).grid(row=4, column=2, padx=10, pady=10)
tk.Button(root, text="Limpar Campos", command=limpar_campos).grid(row=5, column=0, padx=10, pady=10)

# Lista de clientes
lista_clientes = tk.Listbox(root, height=10, width=50)
lista_clientes.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

# Exibir os clientes ao iniciar
mostrar_clientes()

# Iniciar a aplicação
root.mainloop()




















# CREATE =  CRIAR 
# READ   =  LER
# UPDATE = ATUALIZAR 
# DELETE =  DELETAR