# Código-fonte — Saúde Antes da Emergência

## 1. Objetivo

Esta pasta será destinada ao código-fonte da aplicação Saúde Antes da Emergência.

A aplicação terá como finalidade disponibilizar informações e indicadores territoriais de saúde por meio de uma interface acessível a gestores públicos e agentes comunitários.

## 2. Responsabilidades previstas

O código-fonte poderá ser organizado em módulos para:

- Consulta aos dados analíticos.
- Integração com o Google BigQuery.
- Processamento de indicadores.
- Regras de negócio do IPTS.
- Serviços de backend.
- Interface da aplicação.
- Autenticação e controle de acesso.

## 3. Organização proposta

```text
src/
├── README.md
├── backend/
├── frontend/
├── services/
├── models/
└── utils/
```

Essa estrutura é uma proposta inicial e poderá ser ajustada conforme a tecnologia escolhida para a aplicação.

## 4. Integração com Google Cloud

A aplicação deverá utilizar os recursos analíticos do Google Cloud, especialmente o BigQuery, respeitando as permissões e os mecanismos de autenticação configurados.

A integração deverá priorizar consultas controladas e acesso somente às informações necessárias.

## 5. Segurança

- Não armazenar credenciais no código.
- Utilizar variáveis de ambiente ou mecanismos seguros de configuração.
- Restringir permissões de acesso.
- Evitar exposição de dados individuais.
- Registrar operações relevantes.
- Seguir as diretrizes de LGPD e governança do projeto.

## 6. Estado atual

A aplicação web ainda está em fase de planejamento. Esta pasta será utilizada para organizar os módulos de implementação quando o desenvolvimento da interface e do backend começar.

**Projeto:** Saúde Antes da Emergência  
**Status:** Estrutura preparada para desenvolvimento futuro
