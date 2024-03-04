"""
EXERCÍCIO 093: Cadastro de Jogador de Futebol

Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

def imprimir(jogador, numPartidas):
    print("-=" * 30)
    print(jogador)
    print("-=" * 30)
    for k, v in jogador.items():
        print(f"O campo {k} tem o valor {v}")
    print("-=" * 30)
    print(f"O jogador {jogador['nome']} jogou {numPartidas}.")

    count = 0
    for i in jogador["gols"]:
        print(f"\tNa partida {count}, fez {i}")
        count += 1


def leitura():
    jogador = {}
    jogador["nome"] = str(input("Nome do jogador: ").strip().capitalize())
    jogador["numPartidas"] = int(
        input(f'Quantas partidas {jogador["nome"]} jogou? ').strip()
    )

    gols = []
    for i in range(jogador["numPartidas"]):
        gols.append(int(input(f"\tQuantos gols na partida {i+1}? ").strip()))
    jogador["gols"] = gols

    totalDeGols = i = 0
    for i in jogador["gols"]:
        totalDeGols += i
    jogador["total"] = totalDeGols

    return jogador


def main():
    infoJogador = leitura()
    numPartidas = infoJogador["numPartidas"]
    del infoJogador["numPartidas"]
    imprimir(infoJogador, numPartidas)
    return 0


if __name__ == "__main__":
    main()
