import sqlite3

def init_db():
    conn = sqlite3.connect('cinema.db')
    cursor = conn.cursor()

    # Tabela de Cinemas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cinemas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            endereco TEXT,
            capacidade_total INTEGER NOT NULL
        )
    ''')

    # Tabela de Filmes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS filmes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            duracao INTEGER NOT NULL,
            genero TEXT,
            diretor TEXT,
            elenco TEXT
        )
    ''')

    # Tabela de Sessões
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sessoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_filme INTEGER NOT NULL,
            id_cinema INTEGER NOT NULL,
            data_hora TEXT NOT NULL,
            publico_registrado INTEGER DEFAULT 0,
            FOREIGN KEY (id_filme) REFERENCES filmes (id),
            FOREIGN KEY (id_cinema) REFERENCES cinemas (id)
        )
    ''')

    # Inserindo dados iniciais para teste (Seed)
    cursor.execute("INSERT OR IGNORE INTO cinemas (id, nome, capacidade_total) VALUES (1, 'Cine Tech Matriz', 100)")
    cursor.execute("INSERT OR IGNORE INTO filmes (id, titulo, duracao) VALUES (1, 'Blade Runner 2049', 164)")
    cursor.execute("INSERT OR IGNORE INTO sessoes (id, id_filme, id_cinema, data_hora) VALUES (1, 1, 1, '2026-05-10 20:00')")

    conn.commit()
    conn.close()
    print("🚀 Banco de dados e tabelas criados com sucesso!")

if __name__ == "__main__":
    init_db()
