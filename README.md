📊 Análise Estatística de Futebol com Python

Este projeto tem como objetivo aplicar conceitos básicos de programação em Python e estatística para realizar uma análise simples de dados de futebol.
Ele foi desenvolvido de forma didática, pensando em aprendizado progressivo, desde a leitura de dados até a criação de uma tabela de campeonato.

Os dados utilizados representam partidas fictícias de futebol e estão organizados em um arquivo CSV, que é lido e processado pelo Python.

🎯 Objetivos do projeto

Aprender os fundamentos de Python aplicados à análise de dados

Trabalhar com arquivos CSV

Calcular estatísticas comuns do futebol

Simular uma tabela de campeonato usando regras reais (3–1–0)

Este projeto não utiliza machine learning, focando exclusivamente em estatística descritiva e lógica de programação.

🗂️ Estrutura do projeto

O projeto está organizado da seguinte forma:

analise_futebol/
│
├── partidas.csv
└── analise.py

📄 Dados utilizados

O arquivo CSV contém as seguintes colunas:

rodada: número da rodada

time_casa: time mandante

time_fora: time visitante

gols_casa: gols do time da casa

gols_fora: gols do time visitante

Esses dados são usados como base para todos os cálculos estatísticos do projeto.

🧮 Análises realizadas

O programa realiza as seguintes análises:

📊 Estatísticas gerais

Média de gols por jogo

Total de gols por partida

⚽ Estatísticas por time

Gols marcados

Gols sofridos

Saldo de gols

🏆 Campeonato

Número de vitórias, empates e derrotas

Pontuação seguindo o sistema 3–1–0

Aproveitamento (% de pontos conquistados)

Ranking de classificação por pontos

Todas as estatísticas são calculadas percorrendo os dados das partidas e aplicando regras reais do futebol.

🧠 Conceitos aplicados

Durante o desenvolvimento do projeto, foram utilizados:

Leitura de arquivos CSV com pandas

Estruturas de dados (dicionários)

Laços de repetição (for)

Condições (if / elif / else)

Ordenação de dados para criação de rankings

Cálculo de porcentagens e métricas esportivas

esportivas

🚀 Possíveis evoluções

Este projeto pode ser facilmente expandido para incluir:

Critérios de desempate (saldo de gols, gols marcados)

Tabela ordenada por múltiplos critérios

Visualização de dados com gráficos

Estatísticas por jogador

Uso mais avançado do pandas

📌 Observação final

Este projeto tem fins educacionais e foi desenvolvido como parte do aprendizado em programação e análise de dados aplicados ao futebol.


partidas.csv: contém os dados das partidas (rodada, times e gols)

analise.py: script principal com toda a lógica de análise
