# Notebooks — Saúde Antes da Emergência

## 1. Objetivo

Esta pasta reúne os notebooks utilizados no processamento, preparação, exploração e validação dos dados do projeto Saúde Antes da Emergência.

Os notebooks foram desenvolvidos principalmente em Python e executados no Google Colab.

## 2. Finalidade

Os notebooks apoiam as seguintes atividades:

- Leitura de arquivos públicos.
- Conversão de formatos.
- Limpeza e padronização dos dados.
- Tratamento de valores ausentes.
- Padronização de códigos municipais.
- Agregação de informações por município e período.
- Validação de cobertura e consistência.
- Preparação de arquivos para importação no BigQuery.

## 3. Fontes processadas

Os procedimentos abrangem:

- SINAN: dengue, tuberculose, HIV em adultos e leptospirose.
- INMET: precipitação, temperatura e umidade.
- IBGE: população e referência territorial.
- CNES: estabelecimentos e serviços de saúde.

## 4. Ambiente de execução

- Linguagem: Python.
- Ambiente auxiliar: Google Colab.
- Ambiente analítico: Google BigQuery.

## 5. Organização recomendada

Os notebooks devem utilizar nomes descritivos e, preferencialmente, numeração sequencial.

Exemplo de organização futura:

```text
notebooks/
├── README.md
├── 01_processamento_sinan.ipynb
├── 02_processamento_inmet.ipynb
├── 03_preparacao_ibge.ipynb
├── 04_processamento_cnes.ipynb
└── 05_validacao_integracao.ipynb
```

Os nomes acima são uma proposta de organização e não significam que todos esses arquivos já estejam publicados.

## 6. Boas práticas

- Documentar objetivo e fonte de cada notebook.
- Separar etapas de coleta, tratamento e validação.
- Registrar parâmetros e filtros utilizados.
- Evitar credenciais diretamente no código.
- Não publicar arquivos brutos ou dados pessoais.
- Registrar resultados relevantes e limitações.
- Manter consistência entre o notebook e a documentação técnica.

## 7. Reprodutibilidade

Sempre que possível, os notebooks deverão registrar:

- Data de processamento.
- Fonte dos arquivos.
- Período de referência.
- Bibliotecas utilizadas.
- Critérios de seleção.
- Arquivos de saída.
- Validações executadas.

**Projeto:** Saúde Antes da Emergência  
**Linguagem:** Python  
**Status:** Em organização
