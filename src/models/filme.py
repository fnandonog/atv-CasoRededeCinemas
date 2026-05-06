class Filme:
    def __init__(self, id=None, titulo="", duracao=0, genero="", diretor="", elenco=""):
        self.id = id
        self.titulo = titulo
        self.duracao = duracao  # em minutos
        self.genero = genero
        self.diretor = diretor
        self.elenco = elenco

    def __repr__(self):
        return f"<Filme {self.titulo}>"
