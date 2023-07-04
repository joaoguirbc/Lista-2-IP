frase = ""

num_garrafas = 20

estoque_final = 1

while frase != "O InterCIn acabou!!! Vamos verificar nosso estoque de bebidas" and num_garrafas >= 0:
    frase = str(input())
    garrafas_necessarias = 0
    if frase == "Acabou uma partida e precisamos da seguinte quantidade de garrafas para matar a sede dos jogadores":
        num_jogadores = int(input())
        if num_jogadores > num_garrafas:
            garrafas_necessarias = num_jogadores - num_garrafas
            print(f"Não teremos água para todos os jogadores... Temos que garantir {garrafas_necessarias} garrafas!!")
            num_garrafas += num_garrafas - num_jogadores
            if num_garrafas < 0:
                print("Por questões logísticas, teremos que acabar com os jogos...")
        else:
            num_garrafas -= num_jogadores

    if frase == "Encham o cooler! O jogo vai começar!!!!":
        print("Geladeira cheia!")
        num_garrafas += 15

    if frase == "Timeout da partida! Verifiquem quantas garrafas pediram aos voluntários":
        quantidade_1 = int(input())
        quantidade_2 = int(input())
        quantidade_3 = int(input())
        quantidade_4 = int(input())
        quantidade_5 = int(input())
        quantidade_total = (quantidade_1 + quantidade_2 + quantidade_3 + quantidade_4 + quantidade_5)
        if quantidade_total > num_garrafas:
            garrafas_faltantes = quantidade_total - num_garrafas
            print(f"Faltaram {garrafas_faltantes} garrafas para atender o pedido feito aos voluntários")
            print("Por questões logísticas, teremos que acabar com os jogos...")
            num_garrafas -= quantidade_total
            
        else:
            num_garrafas -= quantidade_total

if num_garrafas > 0:
    print(f"Sobraram {num_garrafas} garrafas, vamos guardar na geladeira :D")
elif num_garrafas == 0:
    print("Vendemos todas as garrafas! Nosso planejamento foi perfeito!")
