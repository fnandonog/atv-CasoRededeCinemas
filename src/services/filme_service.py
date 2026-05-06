from repositories.filme_repository import FilmeRepository
from repositories.sessao_repository import SessaoRepository

class FilmeService:
    def __init__(self):
        self.filme_repo = FilmeRepository()
        self.sessao_repo = SessaoRepository()

    def excluir_filme(self, filme_id):
        # RN03 – Consistência de Dados
        # Não permite excluir se houver sessões vinculadas
        if self.sessao_repo.contar_por_filme(filme_id) > 0:
            raise Exception("Não é possível excluir um filme que possui sessões agendadas.")
            
        return self.filme_repo.deletar(filme_id)

    def salvar_filme(self, titulo, duracao, genero, diretor, elenco):
        # Validação simples de dados obrigatórios
        if not titulo or duracao <= 0:
            raise Exception("Dados do filme inválidos.")
            
        return self.filme_repo.inserir(titulo, duracao, genero, diretor, elenco)
