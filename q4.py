num_duplas = int(input())

pontuação_maxima = int(-1000000000000000)
pontuação_minima = int(1000000000000000)

for i in range(1,num_duplas + 1):
    nome_dupla = str(input())
    periodo_dupla = int(input())
    pontos_dupla = int(input())

    pontuacao_final = float(pontos_dupla / periodo_dupla)

    if pontuacao_final > pontuação_maxima:
        pontuação_maxima = pontuacao_final
        vencedor = nome_dupla
        pontos_vencedores = pontuacao_final
    
    if pontuacao_final < pontuação_minima:
        pontuação_minima = pontuacao_final
        perdedor = nome_dupla
        pontos_perdedores = pontuacao_final

print(f"A dupla vencedora foi {vencedor} com a pontuação final de {pontos_vencedores:.2f} pontos.")
print(f"A dupla perdedora foi {perdedor} com a pontuação final de {pontos_perdedores:.2f} pontos.")