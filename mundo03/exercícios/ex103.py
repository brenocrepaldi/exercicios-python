def imprimirJogador(nome="<desconhecido>", gols=0):
    print(f"O jogador {nome} fez {gols} no campeonato")


jogador = str(input("Nome do jogador: ").strip())
gols = str(input("Numero de gols: "))
if gols.isnumeric() == True:
    int(gols)


imprimirJogador(jogador, gols)
