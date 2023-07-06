nome_aluno = input()
nome_professor = input()

partidas_ganhas_aluno = 0
partidas_ganhas_professor = 0

partidas_jogadas = 0

pontos_aluno = 0
pontos_professor = 0

print("E agora, só pela resenha:")
print(f"Melhor de 3 entre: {nome_aluno} e {nome_professor}!")
print("COMEÇOU!")

while partidas_ganhas_aluno < 2 and partidas_ganhas_professor < 2:
    
    while (pontos_aluno < 11 and pontos_professor < 11) or (pontos_aluno - pontos_professor < 2 and pontos_professor - pontos_aluno < 2):
        num = int(input())

        if num % 2 == 0:
            pontos_professor += 1
        else:
            pontos_aluno += 1

        print(f"{pontos_aluno} - {pontos_professor}")
    else:
        partidas_jogadas += 1

    if partidas_jogadas > 0:
        if pontos_aluno > pontos_professor:
            partidas_ganhas_aluno += 1
            print(f"{nome_aluno} ganhou esta partida!")
            print(f"Placar: {nome_aluno} [{partidas_ganhas_aluno}-{partidas_ganhas_professor}] {nome_professor}")
        if pontos_professor > pontos_aluno:
            partidas_ganhas_professor += 1
            print(f"{nome_professor} ganhou esta partida!")
            print(f"Placar: {nome_aluno} [{partidas_ganhas_aluno}-{partidas_ganhas_professor}] {nome_professor}")

    pontos_aluno = 0
    pontos_professor = 0
else:
    print("FIM DA SÉRIE!")
    if partidas_ganhas_aluno > partidas_ganhas_professor:
        print(f"{nome_aluno} ganhou a série! Puro talento!")
    else:
        print(f"{nome_professor} ganhou a série! A experiência ganhou!")