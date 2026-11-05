# saude-antes-da-emergencia
Plataforma de inteligência territorial para apoiar a prevenção da dengue no Brasil.
# Saúde Antes da Emergência

### Inteligência territorial para uma saúde mais justa

## Sobre o projeto

O Saúde Antes da Emergência é uma proposta de plataforma web de inteligência territorial em saúde pública, com foco inicial na prevenção da dengue no Brasil.

A solução pretende integrar dados públicos epidemiológicos, climáticos, demográficos e de infraestrutura de saúde para apoiar gestores públicos e agentes comunitários na identificação de territórios que necessitam de maior atenção preventiva.

## Problema

As informações utilizadas no planejamento de ações de saúde pública estão distribuídas em diferentes bases de dados. A integração dessas informações pode ajudar a transformar dados isolados em conhecimento útil para apoiar decisões e priorizar ações preventivas.

## Objetivo

Desenvolver uma plataforma capaz de organizar, integrar e analisar dados públicos para apoiar a priorização territorial de ações de prevenção da dengue.

## Solução proposta

A plataforma terá como elemento central o **Índice de Prioridade Territorial em Saúde (IPTS)**, uma metodologia em desenvolvimento que buscará combinar diferentes dimensões:

- Epidemiológica: registros e indicadores de dengue.
- Climática: precipitação e temperatura.
- Populacional: população e características demográficas.
- Infraestrutura: estabelecimentos e serviços de saúde.

O índice será definido após a coleta, validação e análise das fontes de dados.

## Público-alvo

- Gestores municipais e estaduais de saúde.
- Agentes comunitários de saúde.
- Equipes de vigilância epidemiológica.
- Instituições públicas de saúde.

## Fontes de dados previstas

| Fonte | Informação |
|---|---|
| SINAN / DATASUS | Dados epidemiológicos |
| IBGE | População e municípios |
| INMET | Dados climáticos |
| CNES | Estabelecimentos de saúde |

## Tecnologias previstas

- Python e Pandas: tratamento e análise de dados.
- Google Cloud Storage: armazenamento de arquivos.
- Google BigQuery: processamento e consulta de dados.
- Looker Studio: visualização de indicadores.
- Google Cloud Run: hospedagem da aplicação web.

## Estrutura do repositório

- `docs/`: documentação técnica e metodológica.
- `notebooks/`: experimentos e análises em Python.
- `src/`: códigos-fonte do projeto.
- `data/`: instruções e informações sobre os dados.
- `dashboards/`: documentação dos painéis.

## Status do projeto

**Em desenvolvimento — fase de preparação do ambiente e levantamento de dados.**

## Responsabilidade e ética

O projeto utilizará dados públicos e agregados, com atenção à LGPD, à qualidade das informações, à transparência metodológica e à prevenção de vieses.

A ferramenta terá caráter de apoio à decisão e não substituirá a avaliação dos profissionais de saúde.

## Projeto acadêmico

Global Solution — FIAP — 2026.2

*Integrantes, turma e RMs serão adicionados após a definição da equipe.*
