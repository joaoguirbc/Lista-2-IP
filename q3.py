frase = ""

num_garrafas = 20

estoque_final = 1

while frase != "O InterCIn acabou!!! Vamos ver nosso estoque de bebidas" and num_garrafas >= 0:
    frase = str(input())
    garrafas_necessarias = 0
    if frase == "Acabou uma partida e os alunos estão com MUITA sede, segue a quantidade de jogadores":
        num_jogadores = int(input())
        if num_jogadores > num_garrafas:
            garrafas_necessarias = num_jogadores - num_garrafas
            num_garrafas = (num_garrafas * 2) - num_jogadores
            print(f"Não teremos água para todos os jogadores... Temos que garantir {garrafas_necessarias} garrafas!!")
            if num_garrafas < 0:
                print("Por questões logísticas, teremos que acabar com os jogos...")  
        else:
            num_garrafas -= num_jogadores

    if frase == "Encham o cooler, vai começar um jogo!!!!":
        print("Geladeira cheia!")
        num_garrafas += 15

    if frase == "Timeout da partida, vamos ver quantas garrafas pediram a cada voluntário":
        quantidade_1 = int(input())
        quantidade_2 = int(input())
        quantidade_3 = int(input())
        quantidade_4 = int(input())
        quantidade_5 = int(input())
        quantidade_total = (quantidade_1 + quantidade_2 + quantidade_3 + quantidade_4 + quantidade_5)
        if quantidade_total > num_garrafas:
            garrafas_necessarias = quantidade_total - num_garrafas
            print(f"Prometemos distribuir {garrafas_necessarias} garrafas e zeramos")
            print("Por questões logísticas, teremos que acabar com os jogos...")
            num_garrafas -= quantidade_total
            
        else:
            num_garrafas -= quantidade_total

if num_garrafas > 0:
    print(f"Notícia boa: sobraram {num_garrafas} garrafas, vamos guardar na geladeira :D")
elif num_garrafas == 0:
    print("Vendemos todas as águas, fizemos uma contagem certeira!!")
else:
    print(f"Estamos devendo {num_garrafas * (-1)} garrafas para os alunos...")