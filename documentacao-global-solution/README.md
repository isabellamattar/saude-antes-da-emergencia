# Global Solution 02/2026
## Cloud Solutions & Scalable Infrastructure

### Projeto utilizado
Saúde Antes da Emergência

## 1. Identificação da equipe

**Turma:** 2TSCPV

| Integrante | RM |
|---|---|
| Isabella Simão Mattar | 562481 |
| Arthur Nishiyama | 566274 |
| Diogo do Nascimento | 561541 |

## 2. Objetivo da atividade

Esta documentação apresenta as atividades técnicas realizadas para atender aos requisitos da Global Solution 02/2026, utilizando o Saúde Antes da Emergência como aplicação de referência.

O foco desta etapa é demonstrar o uso de versionamento, gestão de tarefas, integração contínua, configuração de entrega contínua e infraestrutura em nuvem.

## 3. Repositório e organização

**Repositório:** https://github.com/isabellamattar/saude-antes-da-emergencia

O GitHub foi utilizado para armazenar o código, organizar tarefas, controlar versões e automatizar processos.

Recursos utilizados:
- GitHub Issues para histórias de usuário e tarefas.
- GitHub Projects para acompanhamento do trabalho.
- Branches para desenvolvimento separado.
- Commits para registrar alterações.
- Pull Requests para integrar alterações à branch principal.

Branches utilizadas:
- `main`
- `feat/ci-cd-cloud-run`
- `feat/cd-cloud-run`
- `docs/global-solution`

Pull Requests integrados:
- [PR #1 — Integração contínua](https://github.com/isabellamattar/saude-antes-da-emergencia/pull/1)
- [PR #5 — Configuração de entrega contínua](https://github.com/isabellamattar/saude-antes-da-emergencia/pull/5)
- [PR #6 — Documentação da Global Solution](https://github.com/isabellamattar/saude-antes-da-emergencia/pull/6)

## 4. Integração contínua (CI)

**Arquivo:** `.github/workflows/ci.yml`

Foi implementado um workflow no GitHub Actions, acionado por eventos de `push` e `pull_request`.

Etapas:
1. Checkout do código.
2. Configuração do Python 3.12.
3. Instalação das dependências.
4. Execução dos testes automatizados com Pytest.
5. Construção da imagem Docker.

**Resultado:** os testes automatizados e a construção da imagem Docker foram executados com sucesso nas verificações registradas.

## 5. Entrega contínua (CD)

**Arquivo:** `.github/workflows/deploy.yml`

Foi preparado um workflow para automatizar a implantação da API no Google Cloud Run.

Etapas configuradas:
1. Autenticação no Google Cloud por Workload Identity Federation.
2. Configuração do Google Cloud CLI.
3. Configuração do Docker para o Artifact Registry.
4. Construção da imagem da API.
5. Envio da imagem ao Artifact Registry.
6. Implantação no Cloud Run.

O workflow está integrado à branch `main`, mas sua execução depende da variável `ENABLE_CLOUD_DEPLOY` estar definida como `true`.

**Estado atual:** o workflow de CD foi configurado e integrado à branch principal. A execução do deploy está protegida e ainda não foi realizada.

## 6. Infraestrutura em nuvem

**Provedor:** Google Cloud Platform.

Serviços configurados ou preparados:
- **BigQuery:** armazenamento e consulta dos dados analíticos.
- **Artifact Registry:** repositório para imagens Docker.
- **Cloud Run:** serviço destinado à hospedagem da API, ainda não implantado.
- **IAM:** gerenciamento de permissões.
- **Workload Identity Federation:** autenticação entre GitHub Actions e Google Cloud.
- **Contas de serviço:** identidade de execução da API e identidade utilizada pelo processo de implantação.

A implantação no Cloud Run depende da habilitação do faturamento no projeto Google Cloud, que permanece desativada. Por esse motivo, o deploy não foi executado.

## 7. Evidências e entregas

- [Repositório GitHub](https://github.com/isabellamattar/saude-antes-da-emergencia)
- [GitHub Issues](https://github.com/isabellamattar/saude-antes-da-emergencia/issues)
- [Pull Request #1 — Integração contínua](https://github.com/isabellamattar/saude-antes-da-emergencia/pull/1)
- [Pull Request #5 — Configuração de entrega contínua](https://github.com/isabellamattar/saude-antes-da-emergencia/pull/5)
- [Pull Request #6 — Documentação acadêmica](https://github.com/isabellamattar/saude-antes-da-emergencia/pull/6)
- [GitHub Actions](https://github.com/isabellamattar/saude-antes-da-emergencia/actions)
- [Execução CI após merge do PR #5](https://github.com/isabellamattar/saude-antes-da-emergencia/actions/runs/43441111096)
- [Execução CD protegida após merge do PR #5](https://github.com/isabellamattar/saude-antes-da-emergencia/actions/runs/43441111134)

As capturas de tela complementares da gestão do projeto, versionamento, workflows e infraestrutura em nuvem devem acompanhar esta documentação como evidências da atividade.

## 8. Situação dos requisitos

| Requisito | Situação |
|---|---|
| GitHub Issues e Projects | Implementados |
| Repositório e versionamento | Implementados |
| Branches, commits e Pull Requests | Implementados |
| Testes automatizados | Executados com sucesso |
| Integração contínua (CI) | Validada com sucesso |
| Configuração do CD | Implementada |
| Infraestrutura de apoio no Google Cloud | Preparada |
| Publicação no Cloud Run | Pendente |
| Demonstração de atualização automática em produção | Pendente |
| Documentação e evidências | Em finalização |

## 9. Considerações finais

A atividade permitiu preparar uma estrutura de integração entre GitHub e Google Cloud, com testes automatizados, construção de imagens Docker e configuração de autenticação segura para implantação.

A integração contínua foi validada com sucesso. A entrega contínua foi configurada e integrada à branch principal. Entretanto, a publicação efetiva no Cloud Run e a demonstração de atualização automática em produção permanecem pendentes da habilitação do faturamento e da execução do deploy.

O projeto mantém a documentação acadêmica separada do README principal, preservando a descrição original da solução Saúde Antes da Emergência.
