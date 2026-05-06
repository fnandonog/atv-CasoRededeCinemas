import sqlite3

def get_connection():
    # Cria o arquivo do banco se não existir e retorna a conexão
    conn = sqlite3.connect('cinema.db')
    conn.row_factory = sqlite3.Row  # Permite acessar colunas pelo nome
    return conn
