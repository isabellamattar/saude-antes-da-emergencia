
from fastapi import FastAPI, HTTPException, Query
from google.cloud import bigquery

PROJECT_ID = "vicky-290611"

app = FastAPI(
    title="Saúde Antes da Emergência API",
    description="API de inteligência territorial em saúde",
    version="1.0.0"
)


def get_bigquery_client():
    return bigquery.Client(project=PROJECT_ID)


@app.get("/")
def inicio():
    return {
        "projeto": "Saúde Antes da Emergência",
        "mensagem": "API funcionando!"
    }


@app.get("/api/health")
def health():
    return {
        "status": "ok",
        "api": "online"
    }


@app.get("/api/epidemiologia")
def epidemiologia(
    doenca: str | None = None,
    ano: int | None = None,
    limite: int = Query(default=1000, ge=1, le=5000),
    deslocamento: int = Query(default=0, ge=0)
):
    query = """
        SELECT
            codigo_ibge,
            municipio,
            uf,
            ano,
            doenca,
            taxa_notificacoes_100mil,
            score_percentil,
            faixa_prioridade_relativa
        FROM
            `vicky-290611.saude_antes_emergencia.vw_indicadores_epidemiologicos_consumo`
        WHERE
            (@doenca IS NULL OR UPPER(doenca) = UPPER(@doenca))
            AND (@ano IS NULL OR ano = @ano)
        ORDER BY ano, doenca, municipio
        LIMIT @limite
        OFFSET @deslocamento
    """

    parametros = [
        bigquery.ScalarQueryParameter("doenca", "STRING", doenca),
        bigquery.ScalarQueryParameter("ano", "INT64", ano),
        bigquery.ScalarQueryParameter("limite", "INT64", limite),
        bigquery.ScalarQueryParameter(
            "deslocamento", "INT64", deslocamento
        )
    ]

    try:
        client = get_bigquery_client()

        config = bigquery.QueryJobConfig(
            query_parameters=parametros
        )

        resultado = client.query(
            query,
            job_config=config
        ).result()

        dados = [dict(linha.items()) for linha in resultado]

        return {
            "total_retornado": len(dados),
            "limite": limite,
            "deslocamento": deslocamento,
            "filtros": {
                "doenca": doenca,
                "ano": ano
            },
            "dados": dados
        }

    except Exception as erro:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao consultar BigQuery: {str(erro)}"
        )


@app.get("/api/cobertura")
def cobertura():
    try:
        client = get_bigquery_client()

        query_municipal = """
            SELECT
                codigo_ibge,
                municipio,
                uf,
                quantidade_doencas,
                tem_dengue,
                tem_hiv,
                tem_leptospirose,
                tem_tuberculose,
                doencas_disponiveis,
                classificacao_cobertura
            FROM
                `vicky-290611.saude_antes_emergencia.vw_cobertura_epidemiologica_consumo`
            ORDER BY municipio
        """

        query_nacional = """
            SELECT
                ano,
                doenca,
                total_municipios,
                municipios_com_dados,
                municipios_com_zero,
                municipios_sem_dados,
                cobertura_pct
            FROM
                `vicky-290611.saude_antes_emergencia.vw_cobertura_indicadores_consumo`
            ORDER BY doenca
        """

        dados_municipais = list(
            client.query(query_municipal).result()
        )

        dados_nacionais = list(
            client.query(query_nacional).result()
        )

        return {
            "total_municipios": len(dados_municipais),
            "cobertura_municipal": [
                dict(linha.items()) for linha in dados_municipais
            ],
            "cobertura_por_doenca": [
                dict(linha.items()) for linha in dados_nacionais
            ]
        }

    except Exception as erro:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao consultar cobertura: {str(erro)}"
        )

@app.get("/api/resumo")
def resumo():
    try:
        client = get_bigquery_client()

        query_epidemiologia = """
            SELECT
                COUNT(*) AS total_registros,
                COUNT(DISTINCT codigo_ibge) AS municipios_com_indicadores,
                COUNT(DISTINCT doenca) AS total_doencas,
                MIN(ano) AS ano_inicial,
                MAX(ano) AS ano_final
            FROM
                `vicky-290611.saude_antes_emergencia.vw_indicadores_epidemiologicos_consumo`
        """

        query_municipios = """
            SELECT
                COUNT(*) AS total_municipios,
                COUNTIF(quantidade_doencas > 0)
                    AS municipios_com_indicadores,
                COUNTIF(quantidade_doencas = 0)
                    AS municipios_sem_indicadores
            FROM
                `vicky-290611.saude_antes_emergencia.vw_cobertura_epidemiologica_consumo`
        """

        query_cobertura = """
            SELECT
                doenca,
                ano,
                total_municipios,
                municipios_com_dados,
                municipios_sem_dados,
                cobertura_pct
            FROM
                `vicky-290611.saude_antes_emergencia.vw_cobertura_indicadores_consumo`
            ORDER BY doenca
        """

        dados_epidemiologia = list(
            client.query(query_epidemiologia).result()
        )

        dados_municipios = list(
            client.query(query_municipios).result()
        )

        dados_cobertura = list(
            client.query(query_cobertura).result()
        )

        return {
            "epidemiologia": dict(dados_epidemiologia[0].items()),
            "municipios": dict(dados_municipios[0].items()),
            "cobertura_por_doenca": [
                dict(linha.items()) for linha in dados_cobertura
            ]
        }

    except Exception as erro:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao consultar resumo: {str(erro)}"
        )
        
@app.get("/api/clima")
def clima(
    ano: int | None = None,
    uf: str | None = None,
    com_dados: bool | None = None,
    limite: int = Query(default=1000, ge=1, le=5000),
    deslocamento: int = Query(default=0, ge=0)
):
    try:
        client = get_bigquery_client()

        filtros_sql = """
            WHERE
                (@ano IS NULL OR ano_climatico = @ano)
                AND (@uf IS NULL OR UPPER(uf) = UPPER(@uf))
                AND (
                    @com_dados IS NULL
                    OR tem_dados_climaticos = @com_dados
                )
        """

        parametros = [
            bigquery.ScalarQueryParameter("ano", "INT64", ano),
            bigquery.ScalarQueryParameter("uf", "STRING", uf),
            bigquery.ScalarQueryParameter(
                "com_dados", "BOOL", com_dados
            )
        ]

        query_total = f"""
            SELECT COUNT(*) AS total
            FROM
                `vicky-290611.saude_antes_emergencia.vw_painel_municipal_consumo`
            {filtros_sql}
        """

        query_dados = f"""
            SELECT
                codigo_ibge,
                municipio,
                uf,
                ano_climatico,
                precipitacao_acumulada_mm,
                dias_com_precipitacao,
                temperatura_media_anual_c,
                dias_com_temperatura,
                umidade_media_anual_pct,
                dias_com_umidade,
                estacoes_distintas,
                tem_dados_climaticos
            FROM
                `vicky-290611.saude_antes_emergencia.vw_painel_municipal_consumo`
            {filtros_sql}
            ORDER BY ano_climatico, uf, municipio
            LIMIT @limite
            OFFSET @deslocamento
        """

        parametros_dados = parametros + [
            bigquery.ScalarQueryParameter(
                "limite", "INT64", limite
            ),
            bigquery.ScalarQueryParameter(
                "deslocamento", "INT64", deslocamento
            )
        ]

        total_resultado = list(
            client.query(
                query_total,
                job_config=bigquery.QueryJobConfig(
                    query_parameters=parametros
                )
            ).result()
        )

        dados_resultado = list(
            client.query(
                query_dados,
                job_config=bigquery.QueryJobConfig(
                    query_parameters=parametros_dados
                )
            ).result()
        )

        dados = [
            dict(linha.items()) for linha in dados_resultado
        ]

        return {
            "total_registros": total_resultado[0]["total"],
            "total_retornado": len(dados),
            "limite": limite,
            "deslocamento": deslocamento,
            "filtros": {
                "ano": ano,
                "uf": uf,
                "com_dados_climaticos": com_dados
            },
            "dados": dados
        }

    except Exception as erro:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao consultar clima: {str(erro)}"
        )

@app.get("/api/cnes")
def cnes(
    ano: int | None = None,
    uf: str | None = None,
    com_dados: bool | None = None,
    limite: int = Query(default=1000, ge=1, le=5000),
    deslocamento: int = Query(default=0, ge=0)
):
    try:
        client = get_bigquery_client()

        filtros_sql = """
            WHERE
                (@ano IS NULL OR ano_climatico = @ano)
                AND (@uf IS NULL OR UPPER(uf) = UPPER(@uf))
                AND (
                    @com_dados IS NULL
                    OR tem_dados_cnes = @com_dados
                )
        """

        parametros = [
            bigquery.ScalarQueryParameter("ano", "INT64", ano),
            bigquery.ScalarQueryParameter("uf", "STRING", uf),
            bigquery.ScalarQueryParameter(
                "com_dados", "BOOL", com_dados
            )
        ]

        query_total = f"""
            SELECT COUNT(*) AS total
            FROM
                `vicky-290611.saude_antes_emergencia.vw_painel_municipal_consumo`
            {filtros_sql}
        """

        query_dados = f"""
            SELECT
                codigo_ibge,
                municipio,
                uf,
                ano_climatico,
                total_estabelecimentos_ativos,
                estabelecimentos_municipais,
                estabelecimentos_estaduais,
                estabelecimentos_federais,
                estabelecimentos_dupla_gestao,
                estabelecimentos_sem_esfera,
                estabelecimentos_sus,
                estabelecimentos_publicos_sus,
                estabelecimentos_com_atendimento_ambulatorial_sus,
                tem_dados_cnes,
                data_referencia_cnes
            FROM
                `vicky-290611.saude_antes_emergencia.vw_painel_municipal_consumo`
            {filtros_sql}
            ORDER BY ano_climatico, uf, municipio
            LIMIT @limite
            OFFSET @deslocamento
        """

        parametros_dados = parametros + [
            bigquery.ScalarQueryParameter(
                "limite", "INT64", limite
            ),
            bigquery.ScalarQueryParameter(
                "deslocamento", "INT64", deslocamento
            )
        ]

        total_resultado = list(
            client.query(
                query_total,
                job_config=bigquery.QueryJobConfig(
                    query_parameters=parametros
                )
            ).result()
        )

        dados_resultado = list(
            client.query(
                query_dados,
                job_config=bigquery.QueryJobConfig(
                    query_parameters=parametros_dados
                )
            ).result()
        )

        dados = [
            dict(linha.items()) for linha in dados_resultado
        ]

        return {
            "total_registros": total_resultado[0]["total"],
            "total_retornado": len(dados),
            "limite": limite,
            "deslocamento": deslocamento,
            "filtros": {
                "ano": ano,
                "uf": uf,
                "com_dados_cnes": com_dados
            },
            "dados": dados
        }

    except Exception as erro:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao consultar CNES: {str(erro)}"
        )

@app.get("/api/filtros")
def filtros():
    try:
        client = get_bigquery_client()

        query_epidemiologia = """
            SELECT
                ARRAY_AGG(DISTINCT doenca ORDER BY doenca) AS doencas,
                ARRAY_AGG(DISTINCT ano ORDER BY ano) AS anos
            FROM
                `vicky-290611.saude_antes_emergencia.vw_indicadores_epidemiologicos_consumo`
        """

        query_territorial = """
            SELECT
                ARRAY_AGG(DISTINCT uf IGNORE NULLS ORDER BY uf) AS ufs,
                ARRAY_AGG(
                    DISTINCT ano_climatico
                    ORDER BY ano_climatico
                ) AS anos_climaticos
            FROM
                `vicky-290611.saude_antes_emergencia.vw_painel_municipal_consumo`
        """

        resultado_epi = list(
            client.query(query_epidemiologia).result()
        )

        resultado_territorial = list(
            client.query(query_territorial).result()
        )

        return {
            "doencas": resultado_epi[0]["doencas"],
            "anos_epidemiologicos": resultado_epi[0]["anos"],
            "ufs": resultado_territorial[0]["ufs"],
            "anos_climaticos": resultado_territorial[0]["anos_climaticos"]
        }

    except Exception as erro:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao consultar filtros: {str(erro)}"
        )
