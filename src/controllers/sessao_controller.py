from services.sessao_service import SessaoService

class SessaoController:
    def __init__(self):
        # O Controller instancia ou recebe o serviço responsável
        self.service = SessaoService()

    def programar_nova_sessao(self, id_filme, id_cinema, data_hora):
        """Coleta dados da View e envia para o Service processar"""
        resultado = self.service.criar_sessao(id_filme, id_cinema, data_hora)
        return resultado

    def registrar_presenca(self, sessao_id, qtd_espectadores):
        """Ponto de entrada para o caso de uso 'Registrar Público'"""
        try:
            sucesso = self.service.validar_e_registrar_publico(sessao_id, qtd_espectadores)
            if sucesso:
                return {"status": "sucesso", "msg": "Público registrado com sucesso!"}
        except Exception as e:
            return {"status": "erro", "msg": str(e)}

    def obter_relatorio_por_cinema(self, cinema_id):
        return self.service.gerar_relatorio_publico(cinema_id)
