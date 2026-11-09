# Tratamento e Validação dos Dados — Saúde Antes da Emergência

## 1. Objetivo

Documentar os procedimentos de preparação, transformação, integração e validação aplicados às fontes de dados do projeto.

O processo busca garantir consistência territorial, rastreabilidade e transparência metodológica.

## 2. Ambiente de processamento

O processamento inicial foi realizado com:

- Python.
- Google Colab.
- Bibliotecas de leitura e manipulação de dados.
- Google BigQuery para integração e consultas analíticas.

O Colab foi utilizado como ambiente auxiliar de preparação, enquanto o BigQuery concentra as estruturas analíticas.

## 3. Tratamento dos dados epidemiológicos

Os arquivos SINAN foram obtidos em formato DBC e convertidos para formatos que permitissem leitura e manipulação com Python.

Após a leitura, foram aplicados filtros por ano e critérios específicos de cada agravo.

Os registros foram agregados por município, gerando arquivos municipais utilizados na carga analítica.

### 3.1 Critérios de seleção

| Agravo | Ano | Critério aplicado |
|---|---:|---|
| Dengue | 2025 | NU_ANO = 2025; CLASSI_FIN em 10, 11 ou 12 |
| Tuberculose | 2025 | NU_ANO = 2025 |
| HIV em adultos | 2024 | NU_ANO = 2024; CRITERIO = 901 |
| Leptospirose | 2024 | NU_ANO = 2024; CLASSI_FIN = 1 |

Os filtros refletem a preparação realizada e devem ser acompanhados dos respectivos dicionários oficiais para interpretação correta.

### 3.2 Registros processados

| Agravo | Registros selecionados | Registros com código municipal |
|---|---:|---:|
| Dengue | 1.474.930 | 1.474.925 |
| Tuberculose | 110.969 | 110.969 |
| HIV em adultos | 25.736 | 25.736 |
| Leptospirose | 4.186 | 4.181 |

Os registros sem código municipal válido não foram associados por aproximação.

## 4. Padronização municipal

A integração utiliza os códigos municipais do IBGE como referência territorial.

Procedimentos realizados:

1. Padronização dos códigos.
2. Preparação da tabela de municípios válidos.
3. Associação dos códigos epidemiológicos à referência municipal.
4. Identificação de códigos não encontrados.
5. Registro dos casos sem associação em tabela de auditoria.

A tabela `municipios_validos` contém 5.570 municípios.

### 4.1 Auditoria dos códigos epidemiológicos

| Agravo | Códigos não encontrados | Registros sem associação |
|---|---:|---:|
| Dengue | 4 | 4 |
| Tuberculose | 1 | 3 |
| HIV em adultos | 5 | 6 |
| Leptospirose | 1 | 1 |
| **Total** | **11** | **14** |

Além desses casos, foram identificados dez registros sem código municipal informado: cinco de dengue e cinco de leptospirose.

Os códigos não associados foram registrados para investigação, sem atribuição territorial por suposição.

## 5. Cálculo das taxas epidemiológicas

Foram calculadas taxas de notificações selecionadas por 100 mil habitantes:

Taxa = (Total de notificações selecionadas / População de referência) × 100.000.

O denominador utilizado é a população municipal do Censo 2022.

Essas medidas não devem ser interpretadas automaticamente como incidência, risco individual ou número de novos casos confirmados.

## 6. Tratamento dos dados climáticos

Os arquivos do INMET foram processados a partir de registros horários.

Procedimentos realizados:

- Leitura dos arquivos anuais.
- Identificação de metadados e cabeçalhos.
- Padronização de delimitadores e valores numéricos.
- Conversão de observações horárias em indicadores diários.
- Associação geográfica das estações aos municípios.
- Agregação por município e ano.

### 6.1 Critérios operacionais de validação

Na preparação inicial foram adotados os seguintes critérios:

| Variável | Critério operacional |
|---|---|
| Precipitação | 24 horas válidas no dia |
| Temperatura | Pelo menos 18 horas válidas |
| Umidade | Pelo menos 18 horas válidas |

Esses limites são critérios operacionais definidos para a análise do projeto, não padrões oficiais universais do INMET.

### 6.2 Cobertura climática

A estrutura municipal e anual contempla 16.710 combinações: 5.570 municípios em três anos.

Entretanto, somente 575 municípios apresentaram observações climáticas no período analisado.

A cobertura por variável e ano foi:

| Ano | Precipitação | Temperatura | Umidade |
|---|---:|---:|---:|
| 2023 | 9,32% | 9,53% | 9,43% |
| 2024 | 9,03% | 9,43% | 9,21% |
| 2025 | 8,04% | 8,71% | 8,46% |

A cobertura limitada impede que os dados climáticos sejam tratados como dimensão obrigatória para todos os municípios.

Valores ausentes foram preservados, sem preenchimento automático com zero.

## 7. Tratamento dos dados CNES

O arquivo CNES foi processado em Python e convertido em agregações municipais.

Procedimentos realizados:

- Leitura do arquivo JSON.
- Identificação e padronização dos códigos municipais.
- Verificação de duplicidade de identificadores dos estabelecimentos.
- Associação dos códigos municipais à malha territorial.
- Agregação por município e tipo de estabelecimento.
- Preparação de indicadores relacionados à esfera administrativa e atendimento SUS.

Na preparação inicial, foram identificados 642.268 registros no arquivo original.

Uma regra provisória baseada na ausência de motivo de desativação foi utilizada para selecionar 503.143 registros.

Essa seleção ainda requer validação com o dicionário oficial do CNES. Portanto, o resultado não deve ser apresentado como quantidade definitiva de estabelecimentos ativos.

Também foi identificada uma divergência de cobertura municipal que permanece em investigação.

## 8. Integração no BigQuery

As tabelas preparadas foram importadas para o dataset `saude_antes_emergencia`.

A integração do painel municipal considera:

- Código IBGE.
- Município.
- Unidade da Federação.
- Ano de referência.
- Indicadores epidemiológicos.
- Informações climáticas disponíveis.
- Informações de infraestrutura de saúde em validação.

O painel integrado possui 16.710 linhas, correspondentes a 5.570 municípios em três anos.

Os relacionamentos climáticos são realizados por município e ano, evitando multiplicações indevidas de registros.

## 9. Validação analítica

Foram realizadas auditorias para verificar:

- Quantidade total de registros.
- Quantidade de municípios distintos.
- Duplicidades de códigos.
- Registros sem associação territorial.
- Valores ausentes.
- Cobertura por indicador.
- Consistência entre tabelas integradas.

### 9.1 Cobertura epidemiológica

| Indicador | Ano | Municípios com dados | Cobertura |
|---|---:|---:|---:|
| Dengue | 2025 | 4.815 | 86,45% |
| Tuberculose | 2025 | 4.258 | 76,45% |
| HIV em adultos | 2024 | 2.539 | 45,58% |
| Leptospirose | 2024 | 1.041 | 18,69% |

A cobertura indica municípios com registros associados nas tabelas analíticas, não a confirmação de ocorrência ou ausência da doença nos demais municípios.

## 10. Normalização dos indicadores

Foi criada uma estrutura de normalização epidemiológica utilizando `PERCENT_RANK`, separadamente por doença e ano.

A pontuação resultante varia de 0 a 100 e representa a posição relativa do município entre os municípios com dados disponíveis para aquele indicador.

Essa pontuação:

- Não representa probabilidade de adoecimento.
- Não é uma medida de risco individual.
- Não permite comparação direta entre doenças diferentes.
- Não deve ser somada automaticamente em um índice composto.


**Projeto:** Saúde Antes da Emergência  
**Ambiente analítico:** Google BigQuery  
**Status:** Em desenvolvimento e validação
