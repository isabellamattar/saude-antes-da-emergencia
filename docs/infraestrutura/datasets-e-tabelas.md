# Datasets e Tabelas — Saúde Antes da Emergência

## 1. Objetivo

Documentar a organização lógica das estruturas de dados utilizadas no Google BigQuery.

## 2. Dataset principal

| Propriedade | Valor |
|---|---|
| Projeto | vicky-290611 |
| Dataset | saude_antes_emergencia |
| Região | southamerica-east1 |
| Finalidade | Integração e análise territorial em saúde |

## 3. Tabelas de referência municipal

| Tabela | Descrição |
|---|---|
| municipios | Cadastro municipal original utilizado na preparação |
| municipios_validos | Cadastro municipal validado para integração |

A tabela `municipios_validos` contém 5.570 municípios e é utilizada como referência territorial nas análises.

## 4. Tabelas epidemiológicas

| Tabela | Fonte | Referência |
|---|---|---|
| dengue_2025 | SINAN | 2025 |
| tuberculose_2025 | SINAN | 2025 |
| hiv_2024 | SINAN | 2024 |
| leptospirose_2024 | SINAN | 2024 |

As tabelas analíticas municipais correspondentes são:

- `dengue_2025_analitica`
- `tuberculose_2025_analitica`
- `hiv_2024_analitica`
- `leptospirose_2024_analitica`

Essas estruturas apresentam agregações por município, população de referência e taxas de notificações selecionadas por 100 mil habitantes.

## 5. Tabelas climáticas

| Tabela | Descrição |
|---|---|
| inmet_clima_municipal_anual_staging | Estrutura municipal e anual dos dados climáticos |

A estrutura contempla os anos de 2023 a 2025.

O painel climático possui 16.710 combinações de município e ano, correspondentes a 5.570 municípios em três anos.

A existência de uma linha na estrutura não significa que existam observações climáticas para aquele município e ano.

A cobertura efetiva das variáveis climáticas é limitada e deve ser considerada nas análises.

## 6. Tabelas de integração e indicadores

| Objeto | Finalidade |
|---|---|
| painel_municipal_integrado | Integração municipal e temporal das dimensões disponíveis |
| cobertura_indicadores | Auditoria da cobertura dos indicadores |
| indicadores_epidemiologicos_normalizados | Pontuação relativa por doença e ano |
| visao_indicadores_ipts | Visão analítica de apoio ao desenvolvimento do IPTS |

A normalização epidemiológica é realizada separadamente por doença e ano. Os resultados representam posições relativas entre municípios com dados disponíveis, não probabilidades de adoecimento.

## 7. Tabelas de infraestrutura de saúde

| Tabela | Descrição |
|---|---|
| cnes_municipal_staging | Agregações municipais dos estabelecimentos CNES |
| cnes_tipo_municipal_staging | Agregações por município e tipo de estabelecimento |

A integração do CNES ainda passa por validações de associação territorial e consistência dos indicadores.

## 8. Auditoria

| Tabela | Finalidade |
|---|---|
| auditoria_codigos_nao_associados | Registro de códigos municipais que não puderam ser associados à referência territorial |

Os registros não associados devem permanecer identificados até que exista validação documental.

## 9. Observações metodológicas

- As fontes possuem períodos de referência diferentes.
- Valores ausentes não são automaticamente convertidos em zero.
- As taxas epidemiológicas utilizam população do Censo 2022 como denominador de referência.
- Os dados climáticos possuem cobertura desigual entre municípios.
- Estabelecimentos cadastrados não representam necessariamente capacidade efetiva de atendimento.

