# LGPD, Ética e Uso Responsável dos Dados — Saúde Antes da Emergência

## 1. Objetivo

Este documento estabelece diretrizes para o uso ético, responsável e seguro dos dados utilizados no projeto Saúde Antes da Emergência.

A solução trabalha com informações de saúde pública e dados territoriais, exigindo cuidados especiais com privacidade, segurança, interpretação e comunicação dos resultados.

## 2. Princípios éticos

O projeto adota os seguintes princípios:

- Finalidade: utilizar os dados para apoiar ações de prevenção e vigilância em saúde.
- Necessidade: utilizar apenas as informações necessárias para a finalidade proposta.
- Transparência: documentar fontes, critérios, limitações e métodos.
- Segurança: proteger os dados contra acessos e divulgações indevidas.
- Não discriminação: evitar resultados que estigmatizem municípios ou comunidades.
- Responsabilidade: não apresentar indicadores como diagnósticos ou previsões sem validação adequada.

## 3. Lei Geral de Proteção de Dados

A Lei nº 13.709/2018 (LGPD) estabelece regras para o tratamento de dados pessoais no Brasil.

Dados referentes à saúde são classificados como dados pessoais sensíveis quando relacionados a pessoas identificadas ou identificáveis.

O projeto prioriza a utilização de informações agregadas por município, reduzindo a exposição de informações individuais.

A utilização de dados públicos não elimina a necessidade de avaliar finalidade, necessidade, segurança e riscos de identificação.

## 4. Minimização e proteção de dados

As seguintes diretrizes deverão ser observadas:

- Priorizar bases agregadas.
- Evitar disponibilizar registros individuais de notificações.
- Não publicar identificadores pessoais.
- Não incluir dados sensíveis em arquivos públicos do GitHub.
- Restringir o acesso aos arquivos originais quando necessário.
- Avaliar riscos de reidentificação em municípios com poucos registros.
- Evitar cruzamentos que permitam identificar pessoas indiretamente.

## 5. Riscos éticos identificados

### 5.1 Estigmatização territorial

Municípios com maiores taxas podem ser apresentados de forma negativa, mesmo quando os indicadores refletem diferenças de notificação, cobertura ou acesso ao diagnóstico.

**Mitigação:** contextualizar os resultados, explicar as limitações e evitar classificações simplistas de territórios.

### 5.2 Subnotificação

A ausência de notificações não comprova ausência de doença.

**Mitigação:** preservar valores ausentes, informar a cobertura e evitar interpretar falta de registros como risco zero.

### 5.3 Desigualdade na cobertura de dados

Municípios podem apresentar diferentes níveis de cobertura epidemiológica, climática e cadastral.

**Mitigação:** apresentar indicadores de completude e identificar lacunas de informação.

### 5.4 Interpretação causal indevida

A associação entre indicadores climáticos e epidemiológicos não comprova causalidade.

**Mitigação:** utilizar o clima apenas nas análises com justificativa epidemiológica e evidência adequada.

### 5.5 Viés na normalização

A normalização relativa pode destacar municípios dentro de uma distribuição, sem representar risco absoluto.

**Mitigação:** explicar a metodologia, preservar a comparação por doença e ano e não somar automaticamente pontuações diferentes.

### 5.6 Sensibilidade de informações sobre HIV

Informações relacionadas ao HIV exigem cuidados reforçados para evitar exposição, discriminação ou estigmatização.

**Mitigação:** utilizar exclusivamente agregações adequadas, avaliar riscos de identificação em grupos pequenos e restringir a divulgação de resultados sensíveis.


## 6. Responsabilidade no uso dos resultados

Os indicadores possuem finalidade de apoio ao planejamento e à prevenção em saúde pública.

Decisões de gestão deverão considerar avaliações técnicas adicionais, contexto local e participação dos profissionais responsáveis.

## 7. Referências

- Lei nº 13.709/2018 — Lei Geral de Proteção de Dados Pessoais: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm
- Ministério da Saúde: https://www.gov.br/saude/
- Autoridade Nacional de Proteção de Dados: https://www.gov.br/anpd/

**Projeto:** Saúde Antes da Emergência  
**Área:** Governança, privacidade e ética  
**Status:** Diretrizes documentadas
