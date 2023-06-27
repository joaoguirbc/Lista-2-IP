num_participantes = int(input())

vencedor = ""

pontuacao_maxima = int(-100000000000000)

for i in range(1,num_participantes + 1):
    participante = input()
    pontos = int(input())
    penalidades = int(input())

    pontuacao = pontos - penalidades

    if pontuacao > pontuacao_maxima:
        pontuacao_maxima = pontuacao
        vencedor = participante

print(f"O grande vencedor do torneio foi {vencedor} com um total de {pontuacao_maxima} pontos!")