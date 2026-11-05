# 02 — Fontes de Dados

## 1. Objetivo

Documentar as fontes públicas previstas para a construção da plataforma Saúde Antes da Emergência.

A seleção definitiva dependerá da disponibilidade, qualidade, cobertura territorial e possibilidade de integração dos dados.

## 2. Fontes previstas

### 2.1 SINAN / DATASUS

- **Instituição:** Ministério da Saúde.
- **Utilização:** dados de notificações de dengue.
- **Indicadores previstos:** casos notificados, distribuição temporal e territorial.
- **Acesso:** https://datasus.saude.gov.br/
- **Limitações:** possíveis atrasos, subnotificação, revisões e diferenças na qualidade dos registros.

### 2.2 IBGE

- **Instituição:** Instituto Brasileiro de Geografia e Estatística.
- **Utilização:** identificação dos municípios e dados populacionais.
- **Indicadores previstos:** população estimada e código municipal.
- **Acesso:** https://www.ibge.gov.br/
- **API de localidades:** https://servicodados.ibge.gov.br/api/docs/localidades
- **Limitações:** verificar o ano de referência e a disponibilidade de cada indicador.

### 2.3 INMET

- **Instituição:** Instituto Nacional de Meteorologia.
- **Utilização:** informações meteorológicas.
- **Indicadores previstos:** precipitação e temperatura.
- **Acesso:** https://portal.inmet.gov.br/
- **Limitações:** cobertura desigual das estações e necessidade de associar os registros aos territórios.

### 2.4 CNES

- **Instituição:** Ministério da Saúde.
- **Utilização:** informações sobre estabelecimentos de saúde.
- **Indicadores previstos:** quantidade e distribuição de estabelecimentos cadastrados.
- **Acesso:** https://cnes.datasus.gov.br/
- **Limitações:** cadastro de estabelecimentos não representa, isoladamente, capacidade efetiva, qualidade ou facilidade de acesso aos serviços.

## 3. Padronização

O código oficial do município do IBGE será utilizado como chave de integração entre as bases, sempre que disponível.

Os dados também deverão possuir referência temporal identificada, como ano, mês ou data de atualização.

## 4. Período de análise

O período inicialmente planejado é de 2023 a 2025, sujeito à validação da disponibilidade e consistência das fontes.

Dados de 2026, se utilizados, serão identificados como parciais.

## 5. Critérios de validação

Antes da utilização, cada fonte será avaliada considerando:

- Origem e confiabilidade institucional.
- Data de publicação e atualização.
- Cobertura geográfica.
- Completude dos registros.
- Consistência dos campos.
- Possibilidade de integração com outras fontes.

## 6. Registro das extrações

Para cada conjunto de dados utilizado, serão registrados a fonte, o endereço de acesso, a data de extração, o período de referência e as transformações realizadas.
