from ex import moeda

preco = float(input("Digite o preço: R$").strip().replace(",", "."))
aum = int(input("Digite o valor de aumento(%): ").strip())
dim = int(input("Digite o valor de resução(%): ").strip())

moeda.resumo(preco, aum, dim)
