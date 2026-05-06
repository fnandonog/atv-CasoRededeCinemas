# 📊 Diagrama de Casos de Uso

Este diagrama representa as interações entre os atores (Administrador e Espectador) e as funcionalidades principais do sistema CineManage.
```mermaid
useCaseDiagram
    actor "Administrador / Funcionário" as Admin
    actor "Espectador" as User

    package "CineManage System" {
        usecase "Manter Cadastro de Filmes" as UC1
        usecase "Gerenciar Unidades de Cinema" as UC2
        usecase "Programar Sessões" as UC3
        usecase "Registrar Público da Sessão" as UC4
        usecase "Consultar Relatórios de Público" as UC5
        usecase "Consultar Info de Filmes (Elenco/Gênero)" as UC6
    }

    Admin --> UC1
    Admin --> UC2
    Admin --> UC3
    Admin --> UC4
    Admin --> UC5
    
    User --> UC6
