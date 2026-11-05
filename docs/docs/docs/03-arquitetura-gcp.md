# 03 — Arquitetura Tecnológica

## 1. Objetivo

Descrever a arquitetura proposta para a prova de conceito da plataforma Saúde Antes da Emergência.

## 2. Fluxo geral

O fluxo planejado é:

1. Coleta de dados públicos.
2. Armazenamento dos arquivos originais.
3. Limpeza e padronização dos dados.
4. Integração das diferentes fontes.
5. Cálculo dos indicadores territoriais.
6. Disponibilização dos resultados em dashboards e aplicação web.

<img width="1601" height="439" alt="image" src="https://github.com/user-attachments/assets/90790187-4e09-465d-bac2-17b8397f6df5" />

## 3. Serviços Google Cloud previstos

### Cloud Storage

Armazenamento dos arquivos originais e versões processadas das bases.

### BigQuery

Armazenamento estruturado, integração e consultas analíticas.

### Cloud Run

Hospedagem da aplicação web, caso seja necessário executar o backend na nuvem.

### Cloud Build

Automatização do processo de construção e publicação da aplicação, se utilizada.

### Artifact Registry

Armazenamento das imagens de contêiner utilizadas na publicação.

### Looker Studio

Construção de dashboards e visualizações interativas.

## 4. Tecnologias complementares

- Python: processamento e análise.
- Pandas: manipulação de dados.
- SQL: consultas e integração.
- GitHub: versionamento e documentação.
- Google Colab: ambiente inicial de experimentação.

## 5. Estratégia de implementação

A implementação será incremental.

A primeira etapa será desenvolvida localmente ou no Google Colab, sem necessidade de ativar todos os serviços de nuvem.

Os serviços GCP serão incorporados conforme a necessidade técnica e a disponibilidade de orçamento.

## 6. Cuidados arquiteturais

- Evitar serviços desnecessários na POC.
- Monitorar consumo e faturamento.
- Configurar limites de consulta quando aplicável.
- Separar dados brutos e dados tratados.
- Não armazenar dados pessoais identificáveis sem justificativa e controles adequados.
- Registrar as etapas de processamento.

## 7. Status

Arquitetura proposta. A configuração final será atualizada conforme a implementação e os testes.
