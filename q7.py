num_partidas = int(input())

fase = 0

vitorias_p1 = 0
vitorias_adversario = 0

partidas_jogadas = 0

while partidas_jogadas < num_partidas - 1:
    fase += 1
    num_rodadas = int(input())
    print(f"Vai começar a {fase}º partida. Esse jogo terá {num_rodadas} rodada(s).")
    pontos_p1 = 0
    pontos_adversario = 0

    for i in range(1, num_rodadas + 1):
        habilidade_jogador_p1 = int(input())
        habilidade_adversario = int(input())

        if habilidade_jogador_p1 >= habilidade_adversario:
            pontos_p1 += 1
        elif habilidade_adversario > habilidade_jogador_p1:
            pontos_adversario += 1

    if pontos_p1 > pontos_adversario and pontos_p1 - pontos_adversario < 5:
        vitorias_p1 += 1
        print(f"Fim de jogo! O placar foi {pontos_p1}x{pontos_adversario}")
        print("Vamos para próxima fase!")
    elif pontos_adversario > pontos_p1:
        vitorias_adversario += 1
        print(f"Fim de jogo! O placar foi {pontos_p1}x{pontos_adversario}")
        print("Vamos para próxima fase!")
    elif pontos_p1 == pontos_adversario:
        partidas_jogadas += (10000000 ** 100000)
        print(f"Fim de jogo! O placar foi {pontos_p1}x{pontos_adversario}")
        print("Não foi dessa vez! Treinar pro ano que vem!")
    elif pontos_p1 - pontos_adversario >= 5:
        partidas_jogadas += (10000000 ** 100000)
        print(f"Fim de jogo! O placar foi {pontos_p1}x{pontos_adversario}")
        print("QUE GOLEADAAAA!!! Essa vitória fez os outros times desistirem e a equipe de IP/P1 é a campeã!")

    partidas_jogadas += 1

if partidas_jogadas < (10000000 ** 100000):
    num_rodadas = int(input())
    print(f"Tá na hora da grande final! Esse jogo terá {num_rodadas} rodada(s).")
    pontos_p1 = 0
    pontos_adversario = 0

    for i in range(1,num_rodadas + 1):
        habilidade_jogador_p1 = int(input())
        habilidade_adversario = int(input())

        if habilidade_jogador_p1 >= habilidade_adversario:
            pontos_p1 += 1
        elif habilidade_adversario > habilidade_jogador_p1:
            pontos_adversario += 1

    if pontos_p1 > pontos_adversario:
        print(f"Fim de jogo! O placar foi {pontos_p1}x{pontos_adversario}")
        print("É CAMPEÃO! O TIME DE IP/P1 GARANTIU A TAÇA!")
    elif pontos_adversario >= pontos_p1:
        print(f"Fim de jogo! O placar foi {pontos_p1}x{pontos_adversario}")
        print("Ah não!! Chegaram tão longe mas não foi dessa vez. :(")

        
