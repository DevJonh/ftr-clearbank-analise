
import pandas as pd

LIMITE_SUSPEITO = 10000.00


def carregar_e_validar():

    df = pd.read_csv("transacoes.csv")

    total_lidas = len(df)

    # Converter data
    df["data"] = pd.to_datetime(
        df["data"],
        format="%Y-%m-%d",
        errors="coerce"
    )

    # Converter valor
    df["valor"] = pd.to_numeric(
        df["valor"],
        errors="coerce"
    )

    # Remover cliente vazio
    df["cliente_id"] = df["cliente_id"].fillna("").str.strip()

    df = df[
        df["cliente_id"] != ""
    ]

    # Remover datas inválidas
    df = df[
        df["data"].notna()
    ]

    # Remover valores inválidos
    df = df[
        df["valor"].notna()
    ]

    # Valor maior que zero
    df = df[
        df["valor"] > 0
    ]

    # Tipos válidos
    df = df[
        df["tipo"].isin(
            ["credito", "debito"]
        )
    ]

    linhas_validas = len(df)
    linhas_invalidas = total_lidas - linhas_validas

    return (
        df,
        total_lidas,
        linhas_validas,
        linhas_invalidas
    )


def gerar_metricas(df):

    df["mes"] = df["data"].dt.strftime("%Y-%m")

    quantidade = (
        df.groupby("mes")
        .size()
    )

    total_credito = (
        df[df["tipo"] == "credito"]
        .groupby("mes")["valor"]
        .sum()
    )

    total_debito = (
        df[df["tipo"] == "debito"]
        .groupby("mes")["valor"]
        .sum()
    )

    media = (
        df.groupby("mes")["valor"]
        .mean()
    )

    maior_valor = (
        df.groupby("mes")["valor"]
        .max()
    )

    menor_valor = (
        df.groupby("mes")["valor"]
        .min()
    )

    meses = sorted(df["mes"].unique())

    resumo = {}

    for mes in meses:

        credito = total_credito.get(mes, 0)
        debito = total_debito.get(mes, 0)

        resumo[mes] = {
            "quantidade": int(
                quantidade[mes]
            ),

            "total_credito": float(
                credito
            ),

            "total_debito": float(
                debito
            ),

            "saldo": float(
                credito - debito
            ),

            "media": float(
                media[mes]
            ),

            "maior_valor": float(
                maior_valor[mes]
            ),

            "menor_valor": float(
                menor_valor[mes]
            )
        }

    return resumo


def identificar_suspeitas(df):

    return df[
        df["valor"] > LIMITE_SUSPEITO
    ]


def exibir_relatorio(
    resumo,
    suspeitas,
    total_lidas,
    linhas_validas,
    linhas_invalidas
):

    print("\n===== ANÁLISE COM PANDAS =====")

    print(f"\nTotal de linhas lidas: {total_lidas}")
    print(f"Linhas válidas: {linhas_validas}")
    print(f"Linhas inválidas: {linhas_invalidas}")

    print("\n===== RELATÓRIO MENSAL =====")

    for mes, dados in resumo.items():

        print(f"\nMês: {mes}")

        print(
            f"  Transações: {dados['quantidade']}"
        )

        print(
            f"  Total crédito: R$ {dados['total_credito']:.2f}"
        )

        print(
            f"  Total débito: R$ {dados['total_debito']:.2f}"
        )

        print(
            f"  Saldo: R$ {dados['saldo']:.2f}"
        )

        print(
            f"  Média: R$ {dados['media']:.2f}"
        )

        print(
            f"  Maior valor: R$ {dados['maior_valor']:.2f}"
        )

        print(
            f"  Menor valor: R$ {dados['menor_valor']:.2f}"
        )

    print("\n===== TRANSAÇÕES SUSPEITAS =====")

    if suspeitas.empty:

        print(
            "Nenhuma transação suspeita encontrada."
        )

    else:

        for _, transacao in suspeitas.iterrows():

            print(
                f"ID: {transacao['id']} | "
                f"Cliente: {transacao['cliente_id']} | "
                f"Data: {transacao['data'].strftime('%Y-%m-%d')} | "
                f"Valor: R$ {transacao['valor']:.2f}"
            )


# Execução

df, total_lidas, linhas_validas, linhas_invalidas = carregar_e_validar()

resumo = gerar_metricas(df)

suspeitas = identificar_suspeitas(df)

exibir_relatorio(
    resumo,
    suspeitas,
    total_lidas,
    linhas_validas,
    linhas_invalidas
)
