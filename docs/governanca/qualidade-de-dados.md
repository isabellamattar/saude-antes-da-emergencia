# Governança e Qualidade de Dados — Saúde Antes da Emergência

## 1. Objetivo

Este documento estabelece os princípios e critérios de qualidade utilizados no projeto Saúde Antes da Emergência.

A governança busca garantir que os dados utilizados nas análises sejam consistentes, rastreáveis, compreensíveis e adequados à finalidade proposta.

## 2. Princípios de qualidade

A avaliação da qualidade considera as seguintes dimensões:

| Dimensão | Descrição |
|---|---|
| Completude | Verifica a presença dos campos e registros necessários |
| Consistência | Avalia a coerência entre campos e fontes |
| Unicidade | Identifica registros duplicados indevidamente |
| Validade | Verifica códigos, formatos e domínios esperados |
| Atualidade | Considera o período de referência e a defasagem dos dados |
| Rastreabilidade | Permite identificar a origem e as transformações realizadas |

## 3. Regras de qualidade territorial

O código municipal do IBGE é utilizado como referência principal de integração.

As regras incluem:

- Preservar os códigos como texto.
- Padronizar o formato municipal.
- Verificar a existência do código na referência territorial.
- Não associar códigos desconhecidos por aproximação sem validação.
- Registrar municípios sem correspondência.
- Considerar alterações territoriais entre períodos.

## 4. Regras de qualidade epidemiológica

Os dados do SINAN são avaliados considerando:

- Ano de referência.
- Critérios de seleção por agravo.
- Presença do código municipal.
- Quantidade de notificações selecionadas.
- Cobertura territorial.
- Possíveis atrasos e subnotificações.

As taxas são calculadas por 100 mil habitantes, utilizando a população do Censo 2022 como referência.

Essas taxas representam notificações selecionadas e não devem ser interpretadas automaticamente como incidência.

## 5. Regras de qualidade climática

Os dados do INMET são avaliados considerando:

- Quantidade de observações válidas.
- Disponibilidade por variável.
- Consistência das coordenadas das estações.
- Associação geográfica aos municípios.
- Compatibilidade temporal.
- Cobertura territorial.

A cobertura climática identificada é limitada. Portanto, a ausência de observações não pode ser interpretada como ausência de chuva, temperatura ou umidade.

Os critérios de validação horária utilizados são operacionais e específicos do projeto.

## 6. Regras de qualidade do CNES

A análise dos estabelecimentos considera:

- Identificação única dos estabelecimentos.
- Validação dos códigos municipais.
- Tipo de estabelecimento.
- Esfera administrativa.
- Indicadores relacionados ao atendimento SUS.
- Período de referência do arquivo.

A ausência de motivo de desativação foi utilizada como critério provisório de seleção, ainda sujeito à validação documental.

O número de estabelecimentos cadastrados não representa diretamente a capacidade de atendimento do município.

## 7. Valores ausentes

Valores ausentes devem ser preservados quando não houver evidência suficiente para determinar um valor.

Não converter automaticamente valores nulos em zero.

É necessário distinguir:

- Zero confirmado.
- Ausência de registro.
- Dado não informado.
- Município não associado.
- Indicador não disponível.

Essa distinção evita interpretações equivocadas.

## 8. Auditorias implementadas

Foram realizadas verificações no BigQuery para:

- Quantidade de registros.
- Municípios distintos.
- Duplicidades.
- Códigos não associados.
- Cobertura dos indicadores.
- Consistência da integração temporal.
- Valores mínimos e máximos das taxas.
- Distribuição dos indicadores normalizados.

A tabela `auditoria_codigos_nao_associados` registra códigos que não puderam ser relacionados à referência municipal.

A tabela `cobertura_indicadores` registra a cobertura territorial dos indicadores epidemiológicos.


