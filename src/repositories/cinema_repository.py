from database.connection import get_connection
from models.cinema import Cinema

class CinemaRepository:
    def buscar_por_id(self, cinema_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM cinemas WHERE id = ?', (cinema_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Cinema(**row)
        return None
