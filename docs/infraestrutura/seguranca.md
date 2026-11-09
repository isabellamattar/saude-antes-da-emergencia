# Segurança da Infraestrutura — Saúde Antes da Emergência

## 1. Objetivo

Estabelecer diretrizes de segurança para armazenamento, processamento, acesso e compartilhamento dos dados utilizados no projeto Saúde Antes da Emergência.

## 2. Princípios de segurança

A infraestrutura deverá observar os seguintes princípios:

- Confidencialidade: proteger informações contra acessos não autorizados.
- Integridade: preservar a consistência e a confiabilidade dos dados.
- Disponibilidade: manter os recursos acessíveis conforme os requisitos do projeto.
- Rastreabilidade: documentar operações e transformações realizadas.

## 3. Controle de acesso

O acesso aos recursos do Google Cloud deverá seguir o princípio do menor privilégio.

Cada usuário deverá possuir somente as permissões necessárias para suas atividades.

A evolução do ambiente deverá considerar o controle de acesso baseado em funções (RBAC).

### Papéis de referência

| Papel | Responsabilidade |
|---|---|
| Administrador | Gerenciar configurações e permissões |
| Engenheiro de dados | Preparar e integrar dados |
| Analista de dados | Consultar e analisar tabelas |
| Visualizador | Consultar painéis e resultados autorizados |

Esses papéis representam uma proposta de organização. Não significam que todos já estejam configurados no ambiente atual.

## 4. Proteção de dados

As fontes utilizadas incluem notificações epidemiológicas, que podem conter informações pessoais e sensíveis.

Por esse motivo:

- Priorizar dados agregados por município.
- Evitar publicar registros individuais.
- Não incluir identificadores pessoais em painéis públicos.
- Restringir o acesso a arquivos originais quando necessário.
- Aplicar minimização de dados.
- Avaliar riscos de reidentificação em agregações pequenas.

## 5. Segurança do GitHub

O repositório público deverá conter somente materiais autorizados para divulgação.

Não devem ser publicados:

- Senhas.
- Chaves de API.
- Tokens de autenticação.
- Credenciais de contas Google.
- Arquivos brutos com dados pessoais.
- Arquivos de configuração que contenham segredos.

O arquivo `.gitignore` deverá impedir o versionamento acidental desses materiais.

## 6. Conformidade e privacidade

O projeto deverá observar a Lei Geral de Proteção de Dados (LGPD), especialmente quanto ao tratamento de dados pessoais e dados pessoais sensíveis relacionados à saúde.

A utilização de informações epidemiológicas deverá respeitar finalidade, necessidade, segurança e prevenção de danos.

## 7. Monitoramento e auditoria

As próximas etapas da infraestrutura deverão considerar:

- Registro de operações relevantes.
- Revisão periódica das permissões.
- Auditoria das consultas e transformações.
- Identificação de alterações nas tabelas.
- Controle de versões dos códigos de processamento.


