time_1 = input()
time_2 = input()

vitorias_t1 = 0
vitorias_t2 = 0

rodada = 1

while vitorias_t1 < 3 and vitorias_t2 < 3:
    pontuacao_t1 = int(input())
    pontuacao_t2 = int(input())
    if pontuacao_t1 > pontuacao_t2:
        vitorias_t1 += 1
        print(f"O vencedor da {rodada}ª rodada foi: {time_1}")
        rodada += 1
    elif pontuacao_t2 > pontuacao_t1:
        vitorias_t2 += 1
        print(f"O vencedor da {rodada}ª rodada foi: {time_2}")
        rodada += 1
else:
    if vitorias_t1 > vitorias_t2:
        print(f"O time {time_1} ganhou a partida final!")
    else:
        print(f"O time {time_2} ganhou a partida final!")