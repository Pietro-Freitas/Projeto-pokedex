import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="treinadores_pokemon"
    )
    

def inserir_treinador(nome, cidade, id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO treinadores (nome, cidade, id) VALUES (%s, %s, %s)", (nome, cidade, id))
    conn.commit()
    conn.close()

def listar_treinadores():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM treinadores")
    dados = cursor.fetchall()
    conn.close()
    return dados

def deletar_treinador(id):
    print("ID recebido para deletar:", id) 
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM treinadores WHERE id = %s", (id,))
    conn.commit()
    conn.close()