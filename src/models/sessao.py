class Sessao:
    def __init__(self, id=None, id_filme=None, id_cinema=None, data_hora="", publico_registrado=0):
        self.id = id
        self.id_filme = id_filme
        self.id_cinema = id_cinema
        self.data_hora = data_hora
        self.publico_registrado = publico_registrado

    def __repr__(self):
        return f"<Sessao ID {self.id} - Filme {self.id_filme}>"
