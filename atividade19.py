# Requisitos  tkinter  -  interface gráfica
# Sqlite3 -  Bancos de dados 
# TTk -  Submódulo do tkinter 
# MessageBox  -  biblioteca que cria uma caixa de dialogo
# Python Puro

import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def conectar():
    return sqlite3.connect('teste.db')

def criar_tabela():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
       CREATE TABLE IF NOT EXISTS usuarios(
       id INTEGER NOT NULL,
       nome TEXT NOT NULL,
       email TEXT NOT NULL                    
       ) 
''')
    conn.commit()
    conn.close()


# CREATE CRIAR
def inserir_usuario():
    nome  = entry_nome.get()
    email = entry_email.get()    
    cpf = entry_cpf.get()
    if nome and email:
        conn = conectar()
        c = conn.cursor()
        c.execute('INSERT INTO usuarios(id, nome, email)  VALUES(?,?,?)',( cpf, nome, email))
        conn.commit()
        conn.close()
        messagebox.showinfo('AVISO', 'DADOS INSERIDOS')
        mostrar_usuario()
    else:
        messagebox.showerror('ERRO', 'ALGO DEU ERRADO')

# READ LER            

def mostrar_usuario():
    for row in tree.get_children():
        tree.delete(row)
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM usuarios')
    usuarios = c.fetchall()
    for usuario in usuarios:
        tree.insert("", "end", values=(usuario[0],usuario[1],usuario[2]))
    conn.close()    
#DELETE  -  DELETAR

def delete_usuario():
    dados_del  = tree.selection()
    if dados_del:
       user_id = tree.item(dados_del)['values'][0]         
       conn = conectar()
       c = conn.cursor()
       c.execute('DELETE FROM usuarios WHERE id = ? ' ,(user_id,))
       conn.commit()
       conn.close()
       messagebox.showinfo('', 'DADO DELETADO')
       mostrar_usuario()
    else:
        messagebox.showerror('ERRO','OCORREU UM ERRO')   

# UPDATE  -  ATUALIZAR 
        
def editar():
    selecao = tree.selection()
    if selecao:
        user_id =  tree.item(selecao)['values'][0]
        novo_nome =  entry_nome.get()
        novo_email = entry_email.get()
        if novo_nome and novo_email:
            conn = conectar()
            c = conn.cursor()
            c.execute('UPDATE usuarios SET nome = ? , email = ? WHERE id = ?',(novo_nome, novo_email, user_id))
            conn.commit()
            conn.close()
            messagebox.showinfo('EDIÇÃO', 'DADOS EDITADOS')
            mostrar_usuario()
        else: 
            messagebox.showerror('Erro','NÃO HOUVE ALTERAÇÃO')
    else:
        messagebox.showwarning('', 'PREENCHA TUDO')

janela = tk.Tk()
janela.configure(bg='#d1d1d1')
janela.title('CRUD')
janela.geometry('700x700')

TITULO = tk.Label(janela,text = 'SISTEMA DE CADASTRO',fg = 'blue',  font=('roboto', 20, 'bold'))
TITULO.grid(row=0,column=0,padx=10, pady=10)

label_CPF  = tk.Label(janela, text='CPF: ', font=('arial', 15))
label_CPF.grid(row=1,column=0, padx=10, pady=10)

entry_cpf =  tk.Entry(janela, font=('arial', 15))
entry_cpf.grid(row=1,column=1, padx=10, pady=10)
#---------------------------------------------------------------------------------
label_nome  = tk.Label(janela, text='NOME: ', font=('arial', 15))
label_nome.grid(row=2,column=0, padx=10, pady=10)

entry_nome = tk.Entry(janela, font=('arial', 15))
entry_nome.grid(row=2,column=1, padx=10, pady=10)
# ---------------------------------------------------------------------------------
label_email  = tk.Label(janela, text='E-MAIL: ', font=('arial', 15))
label_email.grid(row=3,column=0, padx=10, pady=10)

entry_email = tk.Entry(janela, font=('arial', 15))
entry_email.grid(row=3,column=1, padx=10, pady=10)

btn_salvar = tk.Button(janela, text = 'Salvar', font= ('arial', 15), command=inserir_usuario)
btn_salvar.grid(row=5,column=2, padx=2, pady=30) 

btn_editar = tk.Button(janela, text = 'Editar', font= ('arial', 15), command=editar)
btn_editar.grid(row=6,column=2, padx=2, pady=30) 

btn_Deletar = tk.Button(janela, text = 'Deletar', font= ('arial', 15), command=delete_usuario)
btn_Deletar.grid(row=7,column=2, padx=2, pady=30) 


columns = ('ID', 'NOME', 'E-MAIL')
tree = ttk.Treeview(janela, columns=columns, show='headings')
tree.grid(row=8, column=0, columnspan=2,padx=10, pady=10)

for col in columns:
    tree.heading(col, text=col)

criar_tabela()
mostrar_usuario()

janela.mainloop()






















# CREATE =  CRIAR 
# READ   =  LER
# UPDATE = ATUALIZAR 
# DELETE =  DELETAR
