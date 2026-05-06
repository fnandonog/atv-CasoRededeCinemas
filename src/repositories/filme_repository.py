from database.connection import get_connection
from models.filme import Filme

class FilmeRepository:
    def inserir(self, titulo, duracao, genero, diretor, elenco):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO filmes (titulo, duracao, genero, diretor, elenco)
            VALUES (?, ?, ?, ?, ?)
        ''', (titulo, duracao, genero, diretor, elenco))
        conn.commit()
        conn.close()

    def buscar_todos(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM filmes')
        rows = cursor.fetchall()
        conn.close()
        return [Filme(**row) for row in rows]

    def deletar(self, filme_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM filmes WHERE id = ?', (filme_id,))
        conn.commit()
        conn.close()
