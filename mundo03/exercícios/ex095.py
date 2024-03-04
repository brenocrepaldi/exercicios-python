"""
EXERCÍCIO 095: Aprimorando os Dicionários

Aprimore o EXERCÍCIO 093 para que ele funcione com vários jogadores, incluindo
um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""
def imprimirJogador(jogador):
    print(f'--LEVANTAMENTO DO JOGADOR {jogador['nome'].upper()}:')
    print('-'*30)
    count = 1
    for i in jogador['gols']:
        print(f'No jogo {count} fez {i} gols.')
        count += 1
    print('-'*30)


def menu(jogadores):
    while True:
        print('-='*30)
        print('cod ', end='')
        for k in jogadores[0].keys():
            print(f'{k:<15}', end='')
        print()
        print('-'*30)

        codigo = 0
        for jogador in jogadores:
            print(f'{codigo:>3} ',end='')
            for values in jogador.values():
                print(f'{str(values):<15}', end='')
            print()
            codigo += 1 

        print('-'*30)

        opcao = int(input('Mostrar dados de qual jogador? (999 para parar) ').strip())
        if opcao == 999:
            break
        elif opcao in range(codigo):
            imprimirJogador(jogadores[opcao])
        else:
            print(f'ERRO! Não existe jogador com o código {opcao}')


def lerJogadores():
    jogador = {}
    jogador["nome"] = str(input("Nome do jogador: ").strip().capitalize())
    numPartidas = int(input(f'Quantas partidas {jogador['nome']} jogou? ').strip())
    
    gols = []
    for i in range(numPartidas):
        gols.append(int(input(f'\tQuantos gols na partida {i+1}? ').strip()))
    jogador['gols'] = gols 

    totalDeGols = 0
    for v in jogador["gols"]:
        totalDeGols += v
    jogador['total'] = totalDeGols

    return jogador


def main():
    listaJogadores = []
    continuar = True
    while continuar:
        listaJogadores.append(lerJogadores())
        continuar = str(input("Quer continuar? [S/N] ").strip().upper()[0])
        if continuar not in "SN":
            print("ERRO! Digite apenas [S/N]")
        if continuar == "N":
            break
    
    menu(listaJogadores)


if __name__ == "__main__":
    main()

