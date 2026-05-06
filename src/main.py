from controllers.sessao_controller import SessaoController
from database.setup_db import init_db
import os

def menu_principal():
    # Inicializa o banco se não existir
    if not os.path.exists('cinema.db'):
        init_db()

    controller = SessaoController()

    print("\n" + "="*30)
    print("🎬 CINEMANAGE - SISTEMA DE GESTÃO")
    print("="*30)
    
    print("1. Registrar Público da Sessão")
    print("2. Sair")
    
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        print("\n--- REGISTRO DE PÚBLICO ---")
        sessao_id = int(input("ID da Sessão (tente o ID 1): "))
        qtd = int(input("Quantidade de Espectadores: "))
        
        # O Controller coordena a operação
        resultado = controller.registrar_presenca(sessao_id, qtd)
        
        if resultado["status"] == "sucesso":
            print(f"✅ {resultado['msg']}")
        else:
            print(f"❌ ERRO: {resultado['msg']}")
            
    elif opcao == "2":
        print("Finalizando sistema...")
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    menu_principal()
