equipe1_j1 = str(input())
equipe1_j2 = str(input())
equipe2_j1 = str(input())
equipe2_j2 = str(input())

num_partidas = int(input())

partidas_disputadas = 0

total_equipe_1 = 0
total_equipe_2 = 0

vitorias_equipe_1 = 0
vitorias_equipe_2 = 0

print(f"VAMO VER QUEM VAI COMER GRAMA! TEREMOS {num_partidas} PARTIDAS ENTRE:")
print(f"{equipe1_j1} e {equipe1_j2} X {equipe2_j1} e {equipe2_j2}")

while num_partidas > partidas_disputadas:
    pontos_equipe_1 = int(input())
    pontos_equipe_2 = int(input())

    if pontos_equipe_1 >= pontos_equipe_2 and pontos_equipe_2 > 0:
        vitorias_equipe_1 += 1
    elif pontos_equipe_2 > pontos_equipe_1 and pontos_equipe_1 > 0:
        vitorias_equipe_2 += 1
    elif pontos_equipe_1 > pontos_equipe_2 and pontos_equipe_2 == 0:
        print("JOGO ENCERRADO POR DESISTÊNCIA DA EQUIPE 2, QUE VERGONHA")
        partidas_disputadas += (10000000 ** 100000)
        vitorias_equipe_1 += 1
    elif pontos_equipe_2 > pontos_equipe_1 and pontos_equipe_1 == 0:
        print("JOGO ENCERRADO POR DESISTÊNCIA DA EQUIPE 1, QUE VERGONHA")
        partidas_disputadas += (10000000 ** 100000)
        vitorias_equipe_2 += 1

    total_equipe_1 += pontos_equipe_1
    total_equipe_2 += pontos_equipe_2

    partidas_disputadas += 1

pontos_totais_disputa = total_equipe_1 + total_equipe_2

coeficiente_equipe_1 = (total_equipe_1 * (vitorias_equipe_1 / num_partidas))
coeficiente_equipe_2 = (total_equipe_2 * (vitorias_equipe_2 / num_partidas))

if partidas_disputadas < (1000000 ** 100000):
    print(f"CARAMBA! Tivemos um total de {pontos_totais_disputa} bolas ao chão ao longo dessa disputa.")
    if coeficiente_equipe_1 >= coeficiente_equipe_2:
        print(f"{equipe1_j1} e {equipe1_j2} são os grandes vencedores!")
        print(f"Mataram {total_equipe_1} bolas, ganhando {vitorias_equipe_1} partidas")
    elif coeficiente_equipe_2 > coeficiente_equipe_1:
        print(f"{equipe2_j1} e {equipe2_j2} são os grandes vencedores!")
        print(f"Mataram {total_equipe_2} bolas, ganhando {vitorias_equipe_2} partidas")