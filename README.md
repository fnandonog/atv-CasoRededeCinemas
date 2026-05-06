# 🎬 CineManage - Sistema de Gestão de Redes de Cinema

![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-blueviolet?style=for-the-badge)
![Architecture](https://img.shields.io/badge/Architecture-MVC_%2B_Service_%2B_Repository-orange?style=for-the-badge)
![Database](https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite)

## 📌 Sobre o Projeto
Este projeto foi desenvolvido como estudo de caso para a disciplina de **Engenharia de Software**. O objetivo é gerenciar uma rede de cinemas distribuída em diferentes localizações, controlando desde o catálogo de filmes e organização de sessões até o registro de público e relatórios de ocupação.

O foco principal é a aplicação prática de modelagem UML integrada com uma implementação robusta utilizando padrões de projeto (Design Patterns) e arquitetura em camadas.

---

## 🚀 Tecnologias Utilizadas
- **Linguagem:** [Inserir Linguagem, ex: Python / Java / Dart]
- **Persistência:** SQLite
- **Arquitetura:** MVC (Model-View-Controller) + Service + Repository
- **Modelagem:** UML 2.5

---

## 📑 Levantamento de Requisitos

### Requisitos Funcionais (RF)
- **RF01 – Manter Cadastro de Filmes:** Operações de CRUD para títulos, duração, gênero e elenco.
- **RF02 – Gerenciar Unidades de Cinema:** Cadastro de unidades com endereço e capacidade.
- **RF03 – Programar Sessões:** Vinculação de filmes a salas e horários específicos.
- **RF04 – Registrar Público:** Registro diário da quantidade de espectadores por sessão.
- **RF05 – Consultar Relatórios:** Totalização de público por sessão, filme e unidade.

### Regras de Negócio (RN)
- **RN01 – Conflito de Horário:** Não é permitida a sobreposição de sessões na mesma sala (Duração do filme + 20min de intervalo).
- **RN02 – Limite de Capacidade:** O público registrado não pode exceder a capacidade da sala.
- **RN03 – Integridade Referencial:** Um filme com sessões agendadas não pode ser excluído.

---

## 🏗️ Arquitetura e Design
O sistema segue uma estrutura de camadas para garantir a escalabilidade e facilidade de manutenção:

1.  **View:** Interface com o usuário.
2.  **Controller:** Intermédio entre View e lógica de negócio.
3.  **Service:** Onde residem as Regras de Negócio (validações, cálculos).
4.  **Repository:** Responsável pela abstração do acesso aos dados (SQL).
5.  **Model:** Representação das entidades do domínio.

---

## 📊 Modelagem UML (Documentação Técnica)

> *Nota: Os diagramas serão adicionados conforme a evolução das etapas do projeto.*

### 1. Diagrama de Casos de Uso
Representação das interações entre os Atores (Administrador/Espectador) e as funcionalidades do sistema.
### 2. Diagrama de Classes
Principais entidades: `Cinema`, `Filme`, `Sessão`, `Ator`, `Diretor`.
### 3. Diagramas de Sequência
Fluxo de interação para o caso de uso de **Programação de Sessões**.
---

## 🛠️ Como Executar
1. Clone o repositório:
   ```bash
   git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
