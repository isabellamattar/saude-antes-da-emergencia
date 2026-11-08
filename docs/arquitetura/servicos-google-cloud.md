# Serviços Google Cloud — Saúde Antes da Emergência

## 1. Objetivo

Este documento apresenta os serviços do Google Cloud considerados na arquitetura do projeto, suas responsabilidades e o estágio atual de implantação.

## 2. Google Cloud Platform

O Google Cloud Platform (GCP) é a plataforma de infraestrutura escolhida para apoiar o armazenamento, processamento analítico e futura disponibilização da solução.

O desenvolvimento está sendo realizado de forma incremental, priorizando inicialmente os recursos disponíveis no BigQuery Sandbox.

## 3. Serviços utilizados ou previstos

### 3.1 Google BigQuery

**Situação: Implementado**

Serviço utilizado para armazenamento analítico e execução de consultas SQL.

Principais responsabilidades:

- Armazenamento de tabelas estruturadas.
- Integração de fontes públicas.
- Agregações por município e ano.
- Cálculo de taxas e indicadores.
- Auditoria e validação de dados.

Configuração atual:

| Item | Valor |
|---|---|
| Projeto | vicky-290611 |
| Dataset | saude_antes_emergencia |
| Região | southamerica-east1 |
| Modalidade | BigQuery Sandbox |

### 3.2 Google Cloud Storage

**Situação: Planejado**

Serviço previsto para armazenamento de arquivos originais e intermediários.

Possíveis aplicações:

- Organização dos arquivos por fonte.
- Armazenamento de dados brutos.
- Separação entre dados brutos e tratados.
- Preservação de arquivos para reprocessamento.

### 3.3 Cloud Run

**Situação: Planejado**

Serviço previsto para disponibilizar a aplicação web e componentes de backend.

Poderá executar serviços desenvolvidos em Python ou outras tecnologias compatíveis.

### 3.4 Cloud Build

**Situação: Planejado**

Serviço que poderá automatizar etapas de construção e implantação da aplicação.

### 3.5 Artifact Registry

**Situação: Planejado**

Serviço previsto para armazenar imagens de contêineres utilizadas na implantação da aplicação.

### 3.6 Looker Studio

**Situação: Planejado**

Ferramenta prevista para criar painéis interativos conectados aos dados analíticos do BigQuery.

### 3.7 Google Colab

**Situação: Utilizado como ambiente auxiliar**

Embora não seja o serviço de infraestrutura central do GCP, o Colab tem sido utilizado para experimentação e preparação dos arquivos com Python.

## 4. Distribuição de responsabilidades

| Componente | Responsabilidade |
|---|---|
| Python | Tratamento e transformação |
| Google Colab | Execução auxiliar dos notebooks |
| BigQuery | Armazenamento e análise SQL |
| Cloud Storage | Armazenamento de arquivos, previsto |
| Looker Studio | Visualização, prevista |
| Cloud Run | Aplicação web, prevista |
| Cloud Build | Automação de implantação, prevista |
| Artifact Registry | Imagens de contêiner, previsto |

## 5. Considerações sobre custos

A fase inicial utiliza o BigQuery Sandbox, que possui limites próprios e não exige configuração de faturamento.

A implantação de serviços adicionais deverá considerar:

- Custos de armazenamento.
- Volume de consultas.
- Processamento.
- Tráfego de rede.
- Execução da aplicação.
- Retenção dos dados.

A expansão da arquitetura dependerá de avaliação de viabilidade técnica e financeira.

## 6. Evolução da infraestrutura

A evolução prevista é:

1. Consolidar o ambiente analítico no BigQuery.
2. Finalizar a integração e validação dos dados.
3. Avaliar o uso do Cloud Storage.
4. Desenvolver os painéis no Looker Studio.
5. Construir a aplicação web.
6. Avaliar implantação com Cloud Run.
7. Automatizar o processo de implantação.

**Projeto:** Saúde Antes da Emergência  
**Plataforma:** Google Cloud Platform  
**Status:** Em desenvolvimento
