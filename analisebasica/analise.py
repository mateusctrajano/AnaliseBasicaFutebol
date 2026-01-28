#Objetivo inicial:
#Ler dados de partidas
#Calcular estatísticas simples

import pandas as pd

df = pd.read_csv('partidas.csv')
print(df)

# 1 ESTATISTICA DE GOLS MARCADOS E SOFRIDOS POR TIME

gols_marcados = {}
gols_sofridos = {}

for index, jogo in df.iterrows():
    time_casa = jogo["time_casa"]
    time_fora = jogo["time_fora"]
    gols_casa = jogo["gols_casa"]
    gols_fora = jogo["gols_fora"]

    if time_casa not in gols_marcados:
            gols_marcados[time_casa] = 0
            gols_sofridos[time_casa] = 0

    if time_fora not in gols_marcados:
            gols_marcados[time_fora] = 0
            gols_sofridos[time_fora] = 0

    gols_marcados[time_casa] += gols_casa
    gols_sofridos[time_casa] += gols_fora

    gols_marcados[time_fora] += gols_fora
    gols_sofridos[time_fora] += gols_casa

print("Gols marcados por time:")
for time, gols in gols_marcados.items():
    print(time, ":", gols)

print("\nGols sofridos por time:")
for time, gols in gols_sofridos.items():
    print(time, ":", gols)

# 2 SALDO DE GOLS POR TIME E RANKING

saldo_gols = {}

for time in gols_marcados:
    saldo_gols[time] = gols_marcados[time] - gols_sofridos[time]

print("\nSaldo de gols:")
for time, saldo in saldo_gols.items():
    print(time, ":", saldo)

ranking_gols = sorted(
    gols_marcados.items(),
    key=lambda item: item[1],
    reverse=True
)

print("\nRanking de times (gols marcados):")
posicao = 1
for time, gols in ranking_gols:
    print(posicao, "-", time, ":", gols, "gols")
    posicao += 1

# 3 RAKING POR SALDO DE GOLS

ranking_saldo = sorted(
    saldo_gols.items(),
    key=lambda item: item[1],
    reverse=True
)

print("\nRanking de times (saldo de gols):")
posicao = 1
for time, saldo in ranking_saldo:
    print(posicao, "-", time, ":", saldo)
    posicao += 1

# 4 Aproveitamento e pontuação (3–1–0)

estatisticas = {}

for index, jogo in df.iterrows():
    time_casa = jogo["time_casa"]
    time_fora = jogo["time_fora"]
    gols_casa = jogo["gols_casa"]
    gols_fora = jogo["gols_fora"]

    for time in [time_casa, time_fora]:
        if time not in estatisticas:
            estatisticas[time] = {
                "vitorias": 0,
                "empates": 0,
                "derrotas": 0,
                "pontos": 0,
                "jogos": 0
            }
# 5 Atualização das estatísticas de jogos
    estatisticas[time_casa]["jogos"] += 1
    estatisticas[time_fora]["jogos"] += 1

if gols_casa > gols_fora:
        estatisticas[time_casa]["vitorias"] += 1
        estatisticas[time_casa]["pontos"] += 3

        estatisticas[time_fora]["derrotas"] += 1

elif gols_casa < gols_fora:
        estatisticas[time_fora]["vitorias"] += 1
        estatisticas[time_fora]["pontos"] += 3

        estatisticas[time_casa]["derrotas"] += 1

else:
        estatisticas[time_casa]["empates"] += 1
        estatisticas[time_fora]["empates"] += 1

        estatisticas[time_casa]["pontos"] += 1
        estatisticas[time_fora]["pontos"] += 1

# 6 Cálculo do aproveitamento

for time in estatisticas:
    pontos = estatisticas[time]["pontos"]
    jogos = estatisticas[time]["jogos"]
    pontos_possiveis = jogos * 3

    aproveitamento = (pontos / pontos_possiveis) * 100
    estatisticas[time]["aproveitamento"] = round(aproveitamento, 2)

# 7 Tabela final de classificação

print("\nTabela do campeonato:")
for time, dados in estatisticas.items():
    print(
        time,
        "- Pontos:", dados["pontos"],
        "| V:", dados["vitorias"],
        "E:", dados["empates"],
        "D:", dados["derrotas"],
        "| Aproveitamento:", dados["aproveitamento"], "%"
    )

# 8 Ranking final por pontos

ranking_pontos = sorted(
    estatisticas.items(),
    key=lambda item: item[1]["pontos"],
    reverse=True
)

print("\nClassificação:")
posicao = 1
for time, dados in ranking_pontos:
    print(
        posicao, "-",
        time,
        "| Pontos:", dados["pontos"],
        "| Aproveitamento:", dados["aproveitamento"], "%"
    )
    posicao += 1