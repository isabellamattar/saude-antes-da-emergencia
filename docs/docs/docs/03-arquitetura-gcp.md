# 03 — Arquitetura Tecnológica

## 1. Objetivo

Descrever a arquitetura tecnológica proposta para a prova de conceito da plataforma **Saúde Antes da Emergência**, utilizando o Google Cloud Platform (GCP) como infraestrutura principal para armazenamento, processamento, integração e análise dos dados públicos de saúde.

A arquitetura será implementada de forma incremental, priorizando serviços gerenciados, escalabilidade, rastreabilidade e controle de custos.

## 2. Arquitetura geral

O fluxo tecnológico proposto é:

1. **Coleta:** obtenção de dados públicos de fontes como SINAN/DATASUS, IBGE, INMET e CNES.
2. **Armazenamento inicial:** organização e preservação dos arquivos originais em ambiente controlado.
3. **Preparação:** conversão, limpeza e padronização dos dados utilizando Python.
4. **Armazenamento analítico:** disponibilização das bases estruturadas no BigQuery.
5. **Integração:** cruzamento das informações epidemiológicas, demográficas, climáticas e de infraestrutura.
6. **Análise:** cálculo dos indicadores territoriais e desenvolvimento do Índice de Prioridade Territorial em Saúde (IPTS).
7. **Visualização:** construção de dashboards e, posteriormente, disponibilização dos resultados em uma aplicação web.

A arquitetura prevê uma evolução gradual, iniciando com os recursos gratuitos disponíveis e incorporando novos serviços conforme a necessidade.

## 3. Serviços Google Cloud previstos

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/46749ead-7b70-4f6a-9c59-d441e0e3549d" />

### BigQuery

Será o principal ambiente de armazenamento estruturado e análise dos dados.

Responsabilidades:
- Armazenar tabelas municipais e epidemiológicas tratadas.
- Integrar diferentes fontes de dados por meio de SQL.
- Executar consultas analíticas.
- Apoiar o cálculo dos indicadores territoriais.
- Disponibilizar dados para os dashboards.

**Estratégia inicial:** utilizar o BigQuery Sandbox, que permite iniciar consultas e testes sem ativar uma conta de faturamento, respeitando seus limites de utilização.

### Cloud Storage

Será utilizado futuramente para armazenar os arquivos originais e as versões intermediárias e processadas das bases.

Responsabilidades:
- Preservar os arquivos de origem.
- Organizar os dados por fonte, período e etapa de processamento.
- Manter a separação entre dados brutos e tratados.

Sua ativação será avaliada após a definição do orçamento e da configuração de faturamento.

### Cloud Run Jobs

Poderá executar rotinas de processamento Python na nuvem, como:
- Conversão de arquivos.
- Limpeza e padronização.
- Validação dos dados.
- Atualização das tabelas analíticas.

Será incorporado após a validação do processamento e a preparação dos scripts para execução em contêineres.

### Cloud Run

Poderá hospedar o backend da aplicação web, disponibilizando os indicadores e resultados processados para os usuários da plataforma.

Será considerado em uma etapa posterior, quando o MVP web estiver definido.

### Cloud Build

Poderá automatizar a construção e publicação da aplicação e dos processos de processamento de dados.

### Artifact Registry

Será utilizado para armazenar as imagens de contêiner necessárias à execução dos serviços no Cloud Run.

### Looker Studio

Será utilizado para construir dashboards interativos conectados às tabelas do BigQuery, permitindo visualizar indicadores, comparações territoriais, rankings e informações epidemiológicas.

## 4. Tecnologias complementares

- **Python:** processamento, validação e análise dos dados.
- **Pandas:** manipulação e transformação das bases.
- **SQL:** integração e consultas analíticas no BigQuery.
- **Google Colab:** ambiente auxiliar para experimentação, conversão inicial e validação dos dados.
- **GitHub:** versionamento do código, documentação e acompanhamento da evolução do projeto.

## 5. Estratégia de implementação

A implementação será dividida em etapas:

### Etapa 1 — Preparação e validação dos dados
- Coleta das bases públicas.
- Conversão dos arquivos epidemiológicos.
- Limpeza e padronização dos códigos municipais.
- Validação da qualidade e da cobertura dos dados.

### Etapa 2 — Estruturação no Google Cloud
- Configuração do ambiente no GCP.
- Criação dos conjuntos de dados no BigQuery.
- Importação das bases estruturadas.
- Desenvolvimento das consultas SQL de integração.

### Etapa 3 — Análise territorial
- Integração das fontes.
- Construção dos indicadores por doença.
- Desenvolvimento e validação do IPTS.
- Identificação de prioridades territoriais.

### Etapa 4 — Visualização
- Conexão do BigQuery ao Looker Studio.
- Construção de dashboards.
- Desenvolvimento de mapas, rankings e filtros.

### Etapa 5 — Evolução da infraestrutura
- Avaliação da utilização do Cloud Storage.
- Automatização dos processos com Cloud Run Jobs.
- Implementação do backend com Cloud Run.
- Integração de processos de publicação com Cloud Build e Artifact Registry.

## 6. Cuidados arquiteturais

- Priorizar serviços gerenciados e evitar infraestrutura desnecessária na POC.
- Monitorar o consumo e o faturamento dos serviços.
- Utilizar o BigQuery Sandbox enquanto ele atender às necessidades iniciais.
- Separar dados brutos, intermediários e tratados.
- Padronizar códigos municipais e períodos de referência.
- Registrar as etapas de processamento e as regras de transformação.
- Preservar a rastreabilidade das fontes e dos indicadores.
- Não disponibilizar dados pessoais identificáveis nos dashboards.
- Aplicar agregação territorial e controles adicionais de privacidade, especialmente para dados relacionados ao HIV.
- Sinalizar ausência, incompletude e defasagem de dados, evitando interpretar lacunas como ausência de risco.


