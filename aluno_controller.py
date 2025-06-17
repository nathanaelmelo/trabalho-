from tkinter import messagebox
import sqlite3
from database.db import conectar

def inserir_aluno(id_, matricula, nome, data_nascimento, listar_callback, limpar_callback):
    if not id_ or not matricula or not nome or not data_nascimento:
        messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return

    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO alunos VALUES (?, ?, ?, ?)", (id_, matricula, nome, data_nascimento))
        conn.commit()
        messagebox.showinfo("Sucesso", "Aluno inserido com sucesso!")
        listar_callback()
        limpar_callback()
    except sqlite3.IntegrityError:
        messagebox.showerror("Erro", "ID ou matrícula já cadastrados!")
    finally:
        conn.close()

def excluir_aluno(matricula, listar_callback, limpar_callback):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM alunos WHERE matricula = ?", (matricula,))
    if cursor.rowcount:
        messagebox.showinfo("Sucesso", "Aluno excluído.")
        listar_callback()
        limpar_callback()
    else:
        messagebox.showerror("Erro", "Aluno não encontrado.")
    conn.commit()
    conn.close()

def editar_aluno(matricula, nome, data_nascimento, listar_callback, limpar_callback):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE alunos SET nome = ?, data_nascimento = ? WHERE matricula = ?", (nome, data_nascimento, matricula))
    if cursor.rowcount:
        messagebox.showinfo("Sucesso", "Aluno atualizado.")
        listar_callback()
        limpar_callback()
    else:
        messagebox.showerror("Erro", "Aluno não encontrado.")
    conn.commit()
    conn.close()

def buscar_aluno(termo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, matricula, nome, data_nascimento FROM alunos WHERE matricula = ? OR id = ?", (termo, termo))
    row = cursor.fetchone()
    conn.close()
    return row

def listar_alunos(tabela):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, matricula, nome, data_nascimento FROM alunos")
    rows = cursor.fetchall()
    tabela.delete(*tabela.get_children())
    for row in rows:
        tabela.insert("", "end", values=row)
    conn.close()