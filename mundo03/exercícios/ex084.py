"""
EXERCÍCIO 084: Lista Composta e Análise de Dados

Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
infoList = []
keepGoing = "Y"
lowerWeight = greaterWeight = 0

while keepGoing == "Y":
    name = str(input("Name: ").strip().capitalize())
    weight = float(input("Weight: ").strip())
    infoList.append([name, weight])
    keepGoing = str(input("Continue? [Y/N] ").strip().upper())

print("-=" * 30)
print(f"{len(infoList)} users registered.")

for i in infoList:
    if i == infoList[0]:
        greaterWeight = i[1]
        lowerWeight = i[1]
    else:
        if i[1] > greaterWeight:
            greaterWeight = i[1]
        elif i[1] < lowerWeight:
            lowerWeight = i[1]

greaterWeightNames = []
lowerWeightNames = []

for j in infoList:
    if j[1] == greaterWeight:
        greaterWeightNames.append(j[0])
    elif j[1] == lowerWeight:
        lowerWeightNames.append(j[0])

print(f"The bigger weight was {greaterWeight}kg. {greaterWeightNames[::]}")
print(f"The lowest weight was {lowerWeight}kg. {lowerWeightNames[::]}")

