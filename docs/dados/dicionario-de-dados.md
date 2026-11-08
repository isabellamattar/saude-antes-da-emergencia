# Dicionário de Dados — Saúde Antes da Emergência

## 1. Objetivo

Este documento descreve os principais campos utilizados nas estruturas analíticas do projeto, incluindo seus significados, tipos esperados, origens e regras de utilização.

Os tipos apresentados são referências lógicas. Os tipos físicos definitivos devem ser conferidos no esquema de cada tabela do BigQuery.

## 2. Padrão de nomenclatura

Os nomes dos campos utilizam preferencialmente:

- Letras minúsculas.
- Separação de palavras por sublinhado.
- Nomes descritivos.
- Identificação de unidades de medida quando aplicável.

Exemplo: `precipitacao_acumulada_mm`.

## 3. Tabela de referência municipal

**Tabela:** `municipios_validos`

| Campo | Tipo lógico | Descrição | Origem |
|---|---|---|---|
| codigo_ibge | STRING | Código municipal de sete dígitos | IBGE |
| codigo_sinan | STRING | Código municipal no formato utilizado na associação ao SINAN | SINAN / IBGE |
| municipio | STRING | Nome do município | IBGE |
| uf | STRING | Sigla da Unidade da Federação | IBGE |
| populacao_2022 | INTEGER | População municipal do Censo 2022 | IBGE |

**Regras:**

- O código IBGE deve ser preservado como texto para manter zeros à esquerda.
- O cadastro de referência contém 5.570 municípios.
- Registros sem código válido não devem integrar a referência municipal.

## 4. Tabelas epidemiológicas

**Tabelas analíticas:**

- `dengue_2025_analitica`
- `tuberculose_2025_analitica`
- `hiv_2024_analitica`
- `leptospirose_2024_analitica`

| Campo | Tipo lógico | Descrição | Origem |
|---|---|---|---|
| codigo_ibge | STRING | Código municipal IBGE | IBGE |
| codigo_sinan | STRING | Código municipal utilizado na associação | SINAN |
| municipio | STRING | Nome do município | IBGE |
| uf | STRING | Unidade da Federação | IBGE |
| ano_referencia | INTEGER | Ano dos registros selecionados | SINAN |
| total_notificacoes | INTEGER | Quantidade de notificações selecionadas e associadas ao município | SINAN |
| populacao_2022 | INTEGER | População de referência | IBGE |
| taxa_por_100_mil | FLOAT64 | Taxa de notificações selecionadas por 100 mil habitantes | SINAN / IBGE |

**Regra de cálculo:**

`(total_notificacoes / populacao_2022) * 100000`

A taxa não deve ser interpretada automaticamente como incidência.

## 5. Dados climáticos

**Tabela:** `inmet_clima_municipal_anual_staging`

| Campo | Tipo lógico | Descrição | Origem |
|---|---|---|---|
| codigo_ibge | STRING | Código municipal | IBGE |
| name_muni | STRING | Nome do município | IBGE |
| abbrev_state | STRING | Sigla da UF | IBGE |
| ano | INTEGER | Ano de referência | INMET |
| precipitacao_acumulada_mm | FLOAT64 | Acumulação anual de precipitação a partir das médias diárias válidas | INMET |
| dias_com_precipitacao | INTEGER | Quantidade de dias com precipitação válida | INMET |
| temperatura_media_anual_c | FLOAT64 | Média anual das médias diárias de temperatura | INMET |
| dias_com_temperatura | INTEGER | Quantidade de dias com temperatura válida | INMET |
| umidade_media_anual_pct | FLOAT64 | Média anual das médias diárias de umidade | INMET |
| dias_com_umidade | INTEGER | Quantidade de dias com umidade válida | INMET |
| estacoes_distintas | INTEGER | Quantidade de estações distintas consideradas na agregação | INMET |

**Regras:**

- Os valores ausentes devem permanecer nulos.
- A agregação considera as observações disponíveis.
- A cobertura deve ser avaliada antes de utilizar qualquer variável climática.
- Os indicadores não representam necessariamente as condições meteorológicas de todo o território municipal.

## 6. Dados de infraestrutura de saúde

**Tabelas:**

- `cnes_municipal_staging`
- `cnes_tipo_municipal_staging`

Os principais campos utilizados na preparação incluem:

| Campo | Tipo lógico | Descrição | Origem |
|---|---|---|---|
| codigo_ibge | STRING | Código municipal associado | CNES / IBGE |
| municipio | STRING | Nome do município | IBGE |
| uf | STRING | Unidade da Federação | IBGE |
| total_estabelecimentos | INTEGER | Quantidade de registros de estabelecimentos agregados | CNES |
| estabelecimentos_sus | INTEGER | Quantidade classificada como atendimento SUS segundo a regra aplicada | CNES |
| estabelecimentos_publicos_sus | INTEGER | Quantidade classificada como pública e com atendimento SUS | CNES |
| TP_UNIDADE | STRING | Código do tipo de estabelecimento na estrutura por tipo | CNES |

A interpretação dos indicadores depende das regras de seleção e agregação utilizadas.

A quantidade de estabelecimentos não representa diretamente capacidade, qualidade ou acessibilidade dos serviços.

## 7. Indicadores normalizados

**Tabela:** `indicadores_epidemiologicos_normalizados`

| Campo | Tipo lógico | Descrição |
|---|---|---|
| codigo_ibge | STRING | Código municipal |
| ano_referencia | INTEGER | Ano do indicador |
| doenca | STRING | Identificação do agravo |
| taxa_por_100_mil | FLOAT64 | Taxa de notificações selecionadas |
| score_normalizado | FLOAT64 | Pontuação relativa normalizada entre 0 e 100 |

A normalização é realizada separadamente por doença e ano.

A pontuação representa uma posição relativa entre municípios com dados disponíveis e não uma probabilidade de adoecimento.

## 8. Estrutura integrada

**Tabela:** `painel_municipal_integrado`

Essa estrutura organiza os municípios e anos de referência para permitir o cruzamento das dimensões do projeto.

Os principais grupos de campos são:

- Identificação municipal.
- Ano de referência.
- Indicadores epidemiológicos.
- Indicadores climáticos.
- Informações de população.
- Campos de cobertura e disponibilidade, quando aplicáveis.

O esquema físico deve ser consultado diretamente no BigQuery para manter este documento alinhado à versão efetivamente implantada.

## 9. Regras gerais de qualidade

1. Códigos territoriais devem manter seu formato e tamanho padronizados.
2. Campos de ano devem representar o período real da fonte.
3. Valores ausentes não devem ser convertidos automaticamente em zero.
4. Taxas devem utilizar denominadores documentados.
5. Indicadores normalizados devem preservar a doença e o ano de referência.
6. Campos derivados devem possuir regra de cálculo documentada.
7. Tabelas integradas devem respeitar sua granularidade territorial e temporal.

## 10. Atualização do documento

Este dicionário deverá ser atualizado sempre que:

- Novas fontes forem incorporadas.
- Novas tabelas forem criadas.
- Campos forem adicionados ou removidos.
- Regras de transformação forem alteradas.
- A metodologia dos indicadores for revisada.

**Projeto:** Saúde Antes da Emergência  
**Ambiente analítico:** Google BigQuery  
**Status:** Dicionário inicial em desenvolvimento
