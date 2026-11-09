# Google BigQuery — Infraestrutura Analítica

## 1. Objetivo

Este documento registra a configuração e a utilização do Google BigQuery na arquitetura do projeto Saúde Antes da Emergência.

O BigQuery é o ambiente central de armazenamento estruturado e análise dos dados integrados.

## 2. Configuração do ambiente

| Parâmetro | Configuração |
|---|---|
| Plataforma | Google Cloud Platform |
| Projeto GCP | vicky-290611 |
| Serviço | BigQuery |
| Dataset principal | saude_antes_emergencia |
| Localização | southamerica-east1 |
| Região geográfica | São Paulo |
| Modalidade | BigQuery Sandbox |

## 3. Finalidade do BigQuery

O serviço é utilizado para:

- Armazenar dados municipais estruturados.
- Integrar informações de diferentes fontes públicas.
- Executar consultas SQL.
- Calcular taxas de notificações por 100 mil habitantes.
- Construir indicadores normalizados.
- Realizar auditorias de cobertura e consistência.
- Preparar estruturas para visualização analítica.

## 4. Organização dos dados

O dataset concentra tabelas de referência, dados epidemiológicos, informações climáticas, dados de estabelecimentos de saúde e estruturas integradas.

As tabelas são organizadas de acordo com sua finalidade analítica e seu estágio de processamento.

## 5. Integração dos dados

O código municipal do IBGE é utilizado como chave territorial de referência.

As consultas de integração consideram:

- Compatibilidade entre códigos municipais.
- Ano de referência dos dados.
- Granularidade das tabelas.
- Preservação de valores ausentes.
- Verificação de duplicidades e associações.

Para dados climáticos, o relacionamento considera município e ano, evitando multiplicação indevida de registros.

## 6. Consultas e processamento

O SQL é utilizado para:

- Agregações municipais.
- Junções entre tabelas.
- Cálculo de taxas.
- Normalização de indicadores.
- Análise de cobertura.
- Identificação de registros não associados.

As transformações devem ser documentadas para permitir reprodução e auditoria.

## 7. Limitações do ambiente

O projeto utiliza inicialmente o BigQuery Sandbox.

Essa modalidade possui limites próprios de armazenamento, consultas e funcionalidades. A evolução para outros serviços ou modalidades deverá considerar os requisitos técnicos e financeiros.

Não se deve presumir que todos os serviços adicionais do Google Cloud sejam gratuitos.



