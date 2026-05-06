from services.filme_service import FilmeService

class FilmeController:
    def __init__(self):
        self.service = FilmeService()

    def adicionar_filme(self, titulo, duracao, genero, diretor, elenco):
        return self.service.salvar_filme(titulo, duracao, genero, diretor, elenco)

    def listar_em_cartaz(self):
        return self.service.buscar_todos_filmes()
