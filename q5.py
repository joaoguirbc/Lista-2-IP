num_partidas = int(input())

pontos_spicin_girls = 0
pontos_manchester_cin = 0

partidas_jogadas = 0

while pontos_spicin_girls >= 0 and pontos_manchester_cin >= 0 and partidas_jogadas < num_partidas:
    nome_time = str(input())
    num_gols = int(input())
    num_chutes = int(input())
    num_c_amarelos = int(input())
    num_c_vermelhos = int(input())

    pontos_jogo = (num_gols * 10) + (num_chutes * 3) - (num_c_amarelos * 2) - (num_c_vermelhos * 4)

    if num_gols >= (num_chutes * 0.3):
        pontos_jogo += 3

    if num_c_vermelhos >= num_c_amarelos:
        pontos_jogo -= 3

    if nome_time == "Manchester CIn":
        pontos_manchester_cin += pontos_jogo
    elif nome_time == "SpiCIn Girls":
        pontos_spicin_girls += pontos_jogo

    if pontos_manchester_cin < 0:
        print(f"O time Manchester CIn ficou com pontuação negativa. A aposta não é segura, podemos perder nosso dinheiro.")
        
    if pontos_spicin_girls < 0:
        print(f"O time SpiCIn Girls ficou com pontuação negativa. A aposta não é segura, podemos perder nosso dinheiro.")

    partidas_jogadas += 1

if pontos_spicin_girls >= 0 and pontos_manchester_cin >= 0:
    soma_pontos = pontos_manchester_cin + pontos_spicin_girls
    percentual_mcin = float((float(pontos_manchester_cin / soma_pontos)) * 100)
    percentual_spicin = float((float(pontos_spicin_girls / soma_pontos)) * 100)
    
    if percentual_mcin > percentual_spicin:
        percentual_vencedor = percentual_mcin
        time_vencedor = "Manchester CIn"
    elif percentual_spicin > percentual_mcin:
        percentual_vencedor = percentual_spicin
        time_vencedor = "SpiCIn Girls"

    print(f"Com {percentual_vencedor:.2f}% dos pontos, o time {time_vencedor} pode garantir nosso dinheiro na CInBet, é uma das grandes apostas do InterCIn.")
    
