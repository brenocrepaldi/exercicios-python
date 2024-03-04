def moeda(n):
    return f"R${n:.2f}".replace(".", ",")


def metade(n, p=False):
    n /= 2
    if p:
        return moeda(n)
    return n


def dobro(n, p=False):
    n *= 2
    if p:
        return moeda(n)
    return n


def aumentar(n, pt, p=False):
    n = n + n * (pt / 100)
    if p:
        return moeda(n)
    return n


def diminuir(n, pt, p=False):
    n = n - n * (pt / 100)
    if p:
        return moeda(n)
    return n


def resumo(n: float, aum, dim):
    format = "-" * 60
    print(format)
    print("\t\tRESUMO DO VALOR")
    print(format)
    print(f"Preço analisado:\t\t{moeda(n)}")
    print(f"Dobro do preço:\t\t\t{dobro(n, True)}")
    print(f"Metade do preço:\t\t{metade(n, True)}")
    print(f"{aum}% de aumento:\t\t{aumentar(n, aum, True)}")
    print(f"{dim}% de redução:\t\t{diminuir(n, dim, True)}")
    print(format)
