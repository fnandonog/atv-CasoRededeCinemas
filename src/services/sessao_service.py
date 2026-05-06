from repositories.sessao_repository import SessaoRepository
from repositories.cinema_repository import CinemaRepository

class SessaoService:
    def __init__(self):
        self.sessao_repo = SessaoRepository()
        self.cinema_repo = CinemaRepository()

    def validar_e_registrar_publico(self, sessao_id, qtd):
        # Busca a sessão e o cinema vinculado para verificar a capacidade
        sessao = self.sessao_repo.buscar_por_id(sessao_id)
        cinema = self.cinema_repo.buscar_por_id(sessao.id_cinema)

        # RN02 – Limite de Capacidade
        if qtd > cinema.capacidade_total:
            raise Exception(f"Lotação excedida! Capacidade máxima: {cinema.capacidade_total}")

        # Se passou na regra, pede ao repository para salvar
        return self.sessao_repo.atualizar_publico(sessao_id, qtd)

    def criar_sessao(self, id_filme, id_cinema, data_hora):
        # RN01 – Conflito de Horário (Simplificado)
        # Aqui você verificaria se já existe uma sessão naquele cinema/horário
        existe_conflito = self.sessao_repo.verificar_conflito(id_cinema, data_hora)
        
        if existe_conflito:
            raise Exception("Já existe uma sessão programada para este horário nesta unidade.")
            
        return self.sessao_repo.salvar(id_filme, id_cinema, data_hora)
