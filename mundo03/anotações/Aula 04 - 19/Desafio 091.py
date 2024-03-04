"""
DESAFIO 091: Jogo de Dados em Python

Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint
from time import sleep

jogadores = {}

jogadores["1"] = randint(1, 6)
jogadores["2"] = randint(1, 6)
jogadores["3"] = randint(1, 6)
jogadores["4"] = randint(1, 6)

print(jogadores)
