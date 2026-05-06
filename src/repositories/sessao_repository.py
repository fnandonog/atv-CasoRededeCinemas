from database.connection import get_connection
from models.sessao import Sessao

class SessaoRepository:
    def buscar_por_id(self, sessao_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM sessoes WHERE id = ?', (sessao_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Sessao(**row)
        return None

    def atualizar_publico(self, sessao_id, qtd):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE sessoes SET publico_registrado = ? WHERE id = ?', (qtd, sessao_id))
        conn.commit()
        conn.close()
        return True

    def verificar_conflito(self, id_cinema, data_hora):
        conn = get_connection()
        cursor = conn.cursor()
        # Verifica se já existe sessão no mesmo cinema e horário
        cursor.execute('SELECT id FROM sessoes WHERE id_cinema = ? AND data_hora = ?', (id_cinema, data_hora))
        conflito = cursor.fetchone()
        conn.close()
        return conflito is not None

    def contar_por_filme(self, filme_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) as total FROM sessoes WHERE id_filme = ?', (filme_id,))
        total = cursor.fetchone()['total']
        conn.close()
        return total
