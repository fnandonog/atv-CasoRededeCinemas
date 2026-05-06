# 🎬 CineManage - Sistema de Gestão de Redes de Cinema

![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen?style=for-the-badge)
![Language](https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Architecture](https://img.shields.io/badge/Architecture-MVC_%2B_Service_%2B_Repository-00A3FF?style=for-the-badge)
![Database](https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite)

## 📌 Visão Geral
O **CineManage** é um sistema de informação robusto desenvolvido como estudo de caso para a disciplina de **Engenharia de Software**. O projeto visa solucionar os desafios operacionais de uma rede de cinemas, centralizando o controle de sessões, programação de filmes e métricas de público em uma arquitetura escalável e de fácil manutenção.

---

## 🚀 Tecnologias e Ferramentas
*   **Linguagem de Programação:** Python 3.10+
*   **Persistência de Dados:** SQLite
*   **Modelagem de Sistemas:** UML 2.5 (PlantUML)
*   **Versionamento:** Git & GitHub

---

## 🏗️ Arquitetura do Sistema
O projeto utiliza uma arquitetura em camadas para garantir o **Baixo Acoplamento** e a **Alta Coesão**, facilitando a implementação de testes unitários e a evolução do software:

1.  **View:** Interface em modo texto para interação direta com o usuário.
2.  **Controller:** Gerencia o fluxo de dados entre a interface e a lógica de negócio.
3.  **Service:** Camada central onde são aplicadas as **Regras de Negócio** (Validação de lotação e horários).
4.  **Repository:** Abstração da camada de dados, responsável pelas operações CRUD no SQLite.
5.  **Model:** Definição das entidades de domínio (Cinema, Filme e Sessão).

---

## 📑 Requisitos do Negócio

### Requisitos Funcionais (RF)
*   **RF01:** Cadastro e manutenção do catálogo de filmes.
*   **RF02:** Gestão de unidades físicas (Cinemas) e suas capacidades.
*   **RF03:** Agendamento dinâmico de sessões.
*   **RF04:** Registro e controle de público presente.
*   **RF05:** Geração de relatórios de ocupação.

### Regras de Negócio (RN)
*   **RN01 (Conflito):** Proibição de sessões simultâneas na mesma sala (Intervalo obrigatório de 20min).
*   **RN02 (Lotação):** Bloqueio de registros que excedam a capacidade máxima da unidade.
*   **RN03 (Integridade):** Impedimento de exclusão de filmes vinculados a sessões futuras.

---

## 📊 Documentação Técnica (UML)

A documentação detalhada está organizada na pasta `/docs`. Abaixo, os diagramas fundamentais do projeto:

| Artefato | Visualização |
| :--- | :--- |
| **Casos de Uso** | [Visualizar Diagrama](docs/assets/casodeuso.png) |
| **Classes de Domínio** | [Visualizar Diagrama](docs/assets/diagrama-classes.png) |
| **Sequência (Registro)** | [Visualizar Diagrama](docs/assets/sequencia-registrar-publico.png) |
| **Atividade (Programação)** | [Visualizar Diagrama](docs/assets/atividade-programar-sessao.png) |

---

## 🛠️ Instalação e Execução

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/fnandonog/atv-CasoRededeCinemas.git](https://github.com/fnandonog/atv-CasoRededeCinemas.git)
    cd atv-CasoRededeCinemas
    ```

2.  **Acesse a pasta fonte:**
    ```bash
    cd src
