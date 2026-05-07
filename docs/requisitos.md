# 📝 Levantamento de Requisitos e Regras de Negócio

Este documento descreve as funcionalidades e restrições do sistema CineManage, servindo como base para toda a modelagem UML e implementação realizada.

---

## 1. Requisitos Funcionais (RF)
Os requisitos funcionais descrevem o que o sistema deve fazer.

| ID | Requisito | Descrição |
| :--- | :--- | :--- |
| **RF01** | Manter Filmes | O sistema deve permitir o CRUD (Criar, Ler, Atualizar, Deletar) de filmes com título, duração, gênero, elenco e diretor. |
| **RF02** | Manter Cinemas | O sistema deve permitir cadastrar as unidades de cinema, informando endereço e capacidade total de público. |
| **RF03** | Programar Sessões | O sistema deve permitir a criação de sessões, vinculando um filme a um cinema em uma data e hora específica. |
| **RF04** | Registrar Público | O sistema deve permitir que o funcionário informe a quantidade de espectadores presentes após a realização da sessão. |
| **RF05** | Consultar Relatórios | O sistema deve emitir relatórios de público totalizado por sessão, por filme e por unidade de cinema. |

---

## 2. Regras de Negócio (RN)
As regras de negócio são as restrições e políticas que o software deve aplicar.

*   **RN01 – Conflito de Horário:** Não é permitida a criação de duas sessões na mesma sala com horários sobrepostos. O sistema deve considerar a duração do filme e um intervalo de 20 minutos entre sessões.
*   **RN02 – Limite de Lotação:** O registro de público presente em uma sessão jamais poderá ser superior à capacidade total cadastrada para a unidade de cinema correspondente.
*   **RN03 – Consistência de Exclusão:** Um filme não pode ser removido do sistema se houver sessões (ativas ou passadas) vinculadas a ele, para garantir a integridade dos relatórios.
*   **RN04 – Unicidade de Sessão:** Cada sessão deve possuir um identificador único e estar obrigatoriamente vinculada a um filme e a um cinema válido.

---

## 3. Atores Identificados
*   **Administrador / Funcionário:** Responsável pela gestão dos dados e operação do sistema.
*   **Espectador:** Ator que consome as informações de filmes (elenco e gêneros).
