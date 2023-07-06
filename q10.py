num_jogadores = 0

nome_jogador_1 = ""
lane_jogador_1 = ""
elo_jogador_1 = ""
pontos_jogador_1 = 0
nome_jogador_2 = ""
lane_jogador_2 = ""
elo_jogador_2 = ""
pontos_jogador_2 = 0
nome_jogador_3 = ""
lane_jogador_3 = ""
elo_jogador_3 = ""
pontos_jogador_3 = 0
nome_jogador_4 = ""
lane_jogador_4 = ""
elo_jogador_4 = ""
pontos_jogador_4 = 0
nome_jogador_5 = ""
lane_jogador_5 = ""
elo_jogador_5 = ""
pontos_jogador_5 = 0

while num_jogadores < 5:
    nome_jogador = input()
    if nome_jogador == "Bruna":
        print("LOL NÃO!!! TUDO MENOS LOL!!!")
        num_jogadores += 5
    else:
        lane_jogador = input()
        elo_jogador = input()
        if elo_jogador != "Bronze":
            if elo_jogador != "Prata":
                if elo_jogador != "Ouro":
                    if elo_jogador != "Platina":
                        if elo_jogador != "Diamante":
                            if elo_jogador != "Desafiante":
                                print ("Não conheço esse elo, então vou considerar que é um elo ruim.")

    if nome_jogador != "Bruna":
        if lane_jogador != lane_jogador_1:
            if lane_jogador != lane_jogador_2:
                if lane_jogador != lane_jogador_3:
                    if lane_jogador != lane_jogador_4:
                        if lane_jogador != lane_jogador_5:
                            print(f"{nome_jogador} entrou pro time.")
                            num_jogadores += 1
                            if nome_jogador == "Artur":
                                print("Ele tá meio enferrujado...")
                            elif nome_jogador == "Frej":
                                print("Joga muito!")

                            if elo_jogador == "Bronze":
                                pontos_jogador = 1
                            elif elo_jogador == "Prata":
                                pontos_jogador = 2
                            elif elo_jogador == "Ouro":
                                pontos_jogador = 4
                            elif elo_jogador == "Platina":
                                pontos_jogador = 6
                            elif elo_jogador == "Diamante":
                                pontos_jogador = 8
                            elif elo_jogador == "Desafiante":
                                pontos_jogador = 10
                            else:
                                pontos_jogador = 0

                            if num_jogadores == 1:
                                nome_jogador_1 = nome_jogador
                                lane_jogador_1 = lane_jogador
                                elo_jogador_1 = elo_jogador
                                pontos_jogador_1 = pontos_jogador
                            elif num_jogadores == 2:
                                nome_jogador_2 = nome_jogador
                                lane_jogador_2 = lane_jogador
                                elo_jogador_2 = elo_jogador
                                pontos_jogador_2 = pontos_jogador
                            elif num_jogadores == 3:
                                nome_jogador_3 = nome_jogador
                                lane_jogador_3 = lane_jogador
                                elo_jogador_3 = elo_jogador
                                pontos_jogador_3 = pontos_jogador
                            elif num_jogadores == 4:
                                nome_jogador_4 = nome_jogador
                                lane_jogador_4 = lane_jogador
                                elo_jogador_4 = elo_jogador
                                pontos_jogador_4 = pontos_jogador
                            elif num_jogadores == 5:
                                nome_jogador_5 = nome_jogador
                                lane_jogador_5 = lane_jogador
                                elo_jogador_5 = elo_jogador     
                                pontos_jogador_5 = pontos_jogador
                        else:
                            print(f"{nome_jogador} não foi aceito, que pena.")
                    else:
                        print(f"{nome_jogador} não foi aceito, que pena.")
                else:
                    print(f"{nome_jogador} não foi aceito, que pena.")
            else:
                print(f"{nome_jogador} não foi aceito, que pena.")
        else:
            print(f"{nome_jogador} não foi aceito, que pena.")

pontos_time = (pontos_jogador_1 + pontos_jogador_2 + pontos_jogador_3 + pontos_jogador_4 + pontos_jogador_5)

if nome_jogador != "Bruna":
    print("O time está completo.")
    print(f"{nome_jogador_1} - {lane_jogador_1} ({elo_jogador_1})")
    print(f"{nome_jogador_2} - {lane_jogador_2} ({elo_jogador_2})")
    print(f"{nome_jogador_3} - {lane_jogador_3} ({elo_jogador_3})")
    print(f"{nome_jogador_4} - {lane_jogador_4} ({elo_jogador_4})")
    print(f"{nome_jogador_5} - {lane_jogador_5} ({elo_jogador_5})")

    if nome_jogador_1 != "Artur":
        if nome_jogador_2 != "Artur":
            if nome_jogador_3 != "Artur":
                if nome_jogador_4 != "Artur":
                    if nome_jogador_5 != "Artur":
                        if nome_jogador_1 != "Frej":
                            if nome_jogador_2 != "Frej":
                                if nome_jogador_3 != "Frej":
                                    if nome_jogador_4 != "Frej":
                                        if nome_jogador_5 != "Frej":
                                            if pontos_time >= 18:
                                                print("A GENTE VAI GANHAR!!!")
                                            else:
                                                print("Vai dar ruim...")

    if nome_jogador_1 == "Artur":
        if nome_jogador_2 != "Frej":
            if nome_jogador_3 != "Frej":
                if nome_jogador_4 != "Frej":
                    if nome_jogador_5 != "Frej":
                        print("Vai dar ruim...")
    elif nome_jogador_2 == "Artur":
        if nome_jogador_1 != "Frej":
            if nome_jogador_3 != "Frej":
                if nome_jogador_4 != "Frej":
                    if nome_jogador_5 != "Frej":
                        print("Vai dar ruim...")
    elif nome_jogador_3 == "Artur":
        if nome_jogador_1 != "Frej":
            if nome_jogador_2 != "Frej":
                if nome_jogador_4 != "Frej":
                    if nome_jogador_5 != "Frej":
                        print("Vai dar ruim...")
    elif nome_jogador_4 == "Artur":
        if nome_jogador_1 != "Frej":
            if nome_jogador_2 != "Frej":
                if nome_jogador_3 != "Frej":
                    if nome_jogador_5 != "Frej":
                        print("Vai dar ruim...")
    elif nome_jogador_5 == "Artur":
        if nome_jogador_1 != "Frej":
            if nome_jogador_2 != "Frej":
                if nome_jogador_3 != "Frej":
                    if nome_jogador_4 != "Frej":
                        print("Vai dar ruim...")

    if nome_jogador_1 == "Frej":
        if nome_jogador_2 != "Artur":
            if nome_jogador_3 != "Artur":
                if nome_jogador_4 != "Artur":
                    if nome_jogador_5 != "Artur":
                        print("A GENTE VAI GANHAR!!!")
    elif nome_jogador_2 == "Frej":
        if nome_jogador_1 != "Artur":
            if nome_jogador_3 != "Artur":
                if nome_jogador_4 != "Artur":
                    if nome_jogador_5 != "Artur":
                        print("A GENTE VAI GANHAR!!!")
    elif nome_jogador_3 == "Frej":
        if nome_jogador_1 != "Artur":
            if nome_jogador_2 != "Artur":
                if nome_jogador_4 != "Artur":
                    if nome_jogador_5 != "Artur":
                        print("A GENTE VAI GANHAR!!!")
    elif nome_jogador_4 == "Frej":
        if nome_jogador_1 != "Artur":
            if nome_jogador_2 != "Artur":
                if nome_jogador_3 != "Artur":
                    if nome_jogador_5 != "Artur":
                        print("A GENTE VAI GANHAR!!!")
    elif nome_jogador_5 == "Frej":
        if nome_jogador_1 != "Artur":
            if nome_jogador_2 != "Artur":
                if nome_jogador_3 != "Artur":
                    if nome_jogador_4 != "Artur":
                        print("A GENTE VAI GANHAR!!!")

    if nome_jogador_1 == "Frej":
        if nome_jogador_2 == "Artur" or nome_jogador_3 == "Artur" or nome_jogador_4 == "Artur" or nome_jogador_5 == "Artur":
            if pontos_time >= 18:
                print("A GENTE VAI GANHAR!!!")
            else:
                print("Vai dar ruim...")
    elif nome_jogador_2 == "Frej":
        if nome_jogador_1 == "Artur" or nome_jogador_3 == "Artur" or nome_jogador_4 == "Artur" or nome_jogador_5 == "Artur":
            if pontos_time >= 18:
                print("A GENTE VAI GANHAR!!!")
            else:
                print("Vai dar ruim...")
    elif nome_jogador_3 == "Frej":
        if nome_jogador_1 == "Artur" or nome_jogador_2 == "Artur" or nome_jogador_4 == "Artur" or nome_jogador_5 == "Artur":
            if pontos_time >= 18:
                print("A GENTE VAI GANHAR!!!")
            else:
                print("Vai dar ruim...")
    elif nome_jogador_4 == "Frej":
        if nome_jogador_1 == "Artur" or nome_jogador_2 == "Artur" or nome_jogador_3 == "Artur" or nome_jogador_5 == "Artur":
            if pontos_time >= 18:
                print("A GENTE VAI GANHAR!!!")
            else:
                print("Vai dar ruim...")
    elif nome_jogador_5 == "Frej":
        if nome_jogador_1 == "Artur" or nome_jogador_2 == "Artur" or nome_jogador_3 == "Artur" or nome_jogador_4 == "Artur":
            if pontos_time >= 18:
                print("A GENTE VAI GANHAR!!!")
            else:
                print("Vai dar ruim...")