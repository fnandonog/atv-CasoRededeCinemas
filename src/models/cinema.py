class Cinema:
    def __init__(self, id=None, nome="", endereco="", capacidade_total=0):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.capacidade_total = capacidade_total

    def __repr__(self):
        return f"<Cinema {self.nome}>"
