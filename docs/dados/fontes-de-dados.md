# Fontes de Dados — Saúde Antes da Emergência

## 1. Objetivo

Este documento identifica as fontes públicas utilizadas no projeto Saúde Antes da Emergência, descrevendo sua finalidade, conteúdo, período de referência e limitações conhecidas.

A integração dessas fontes permite construir uma visão territorial de diferentes dimensões relacionadas à saúde pública.

## 2. Fontes utilizadas

### 2.1 SINAN — Sistema de Informação de Agravos de Notificação

**Origem:** Ministério da Saúde / DATASUS.

O SINAN reúne notificações de doenças e agravos de interesse para a vigilância em saúde.

No projeto, foram selecionados registros referentes a:

| Agravo | Arquivo de origem | Ano de referência processado |
|---|---|---|
| Dengue | DENGBR25.dbc | 2025 |
| Tuberculose | TUBEBR25.dbc | 2025 |
| HIV em adultos | HIVABR24.dbc | 2024 |
| Leptospirose | LEPTBR24.dbc | 2024 |

Os arquivos foram obtidos em formato DBC e preparados para processamento com Python.

**Critérios de seleção utilizados na preparação:**

- Dengue: ano de notificação 2025 e classificação final com códigos 10, 11 ou 12.
- Tuberculose: ano de notificação 2025.
- HIV em adultos: ano de notificação 2024 e critério de classificação 901.
- Leptospirose: ano de notificação 2024 e classificação final igual a 1.

Os códigos e critérios deverão ser interpretados conforme os dicionários oficiais de cada sistema. A seleção realizada não deve ser descrita como confirmação clínica de todos os registros sem validação adicional.

**Limitações:**

- Possibilidade de subnotificação.
- Atraso entre ocorrência e notificação.
- Revisões e atualizações dos registros.
- Diferenças de preenchimento entre municípios.
- Períodos de referência distintos entre doenças.

### 2.2 INMET — Instituto Nacional de Meteorologia

**Origem:** Instituto Nacional de Meteorologia.

Foram utilizados arquivos meteorológicos de 2023, 2024 e 2025.

As variáveis processadas incluem:

- Precipitação total.
- Temperatura.
- Umidade relativa do ar.
- Código e identificação da estação.
- Latitude e longitude.
- Data e horário das observações.

Os registros horários foram tratados e agregados por estação e dia. Posteriormente, foram associados aos municípios por meio da localização geográfica das estações.

**Limitações:**

- Distribuição desigual das estações pelo território nacional.
- Diferenças de disponibilidade entre anos.
- Ausência de observações em determinados períodos.
- Possíveis alterações históricas de localização ou identificação das estações.

A cobertura climática identificada é insuficiente para representar uniformemente todos os municípios brasileiros. Por isso, os dados climáticos são tratados como dimensão complementar, e não como indicador nacional obrigatório.

### 2.3 IBGE — Instituto Brasileiro de Geografia e Estatística

**Origem:** Instituto Brasileiro de Geografia e Estatística.

O IBGE fornece a referência territorial utilizada na integração dos dados.

Foram utilizados:

- Códigos municipais.
- Nomes dos municípios.
- Unidades da Federação.
- População do Censo Demográfico 2022.
- Malha municipal de referência de 2022.

A população é utilizada como denominador de referência para calcular taxas de notificações por 100 mil habitantes.

**Limitações:**

- A população de 2022 não corresponde necessariamente à população dos anos epidemiológicos de 2024 e 2025.
- Municípios criados após a referência territorial de 2022 exigem tratamento específico.
- Alterações territoriais e códigos não associados precisam ser documentados.

### 2.4 CNES — Cadastro Nacional de Estabelecimentos de Saúde

**Origem:** Ministério da Saúde / DATASUS.

O CNES é utilizado para caracterizar a distribuição territorial dos estabelecimentos de saúde cadastrados.

Foram utilizados campos relacionados a:

- Código do estabelecimento.
- Código municipal.
- Unidade da Federação.
- Tipo de estabelecimento.
- Esfera administrativa.
- Gestão.
- Atendimento ambulatorial pelo SUS.
- Informações cadastrais e de localização.

A preparação inicial resultou em uma base com 503.143 registros classificados provisoriamente como estabelecimentos sem motivo de desativação informado.

Essa regra ainda requer validação semântica com a documentação oficial do CNES antes de ser utilizada como definição definitiva de estabelecimento ativo.

**Limitações:**

- Cadastro não equivale à capacidade efetiva de atendimento.
- Não representa diretamente qualidade dos serviços.
- Não mede tempo de deslocamento ou acessibilidade.
- Informações cadastrais podem apresentar defasagem.
- Estabelecimentos públicos, privados e conveniados devem ser diferenciados.

## 3. Padronização territorial

O código municipal do IBGE é a principal referência para relacionar as fontes.

Os códigos do SINAN e do CNES são tratados conforme seus formatos de origem e associados à referência municipal do IBGE mediante validação.

Registros sem associação confirmada são preservados para auditoria.

## 4. Compatibilidade temporal

As fontes possuem períodos distintos:

| Fonte | Período processado |
|---|---|
| SINAN — Dengue | 2025 |
| SINAN — Tuberculose | 2025 |
| SINAN — HIV em adultos | 2024 |
| SINAN — Leptospirose | 2024 |
| INMET | 2023 a 2025 |
| IBGE — População | Censo 2022 |
| IBGE — Malha municipal | Referência 2022 |
| CNES | Arquivo utilizado na extração inicial; referência mensal deve ser confirmada |

A integração deve preservar o ano de referência de cada fonte e evitar comparações temporais indevidas.

## 5. Uso responsável

As fontes são utilizadas para análises agregadas por município.

Os resultados devem ser interpretados considerando cobertura, qualidade, defasagem e limitações metodológicas.

A ausência de notificações associadas não significa necessariamente ausência da doença no território.

## 6. Referências oficiais

- DATASUS: https://datasus.saude.gov.br/
- IBGE: https://www.ibge.gov.br/
- INMET: https://portal.inmet.gov.br/
- CNES: https://cnes.datasus.gov.br/

**Projeto:** Saúde Antes da Emergência  
**Área:** Dados públicos e inteligência territorial em saúde  
**Status:** Em desenvolvimento
