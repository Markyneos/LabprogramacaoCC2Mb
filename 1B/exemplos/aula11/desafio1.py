# Problema n°1: Duas Somas
# O problema é encontrar dois números em uma lista que somam um
# determinado número alvo. Precisamos retornar os índices desses dois números em qualquer ordem.
# Podemos assumir que existe apenas uma solução válida e não podemos usar o mesmo elemento duas vezes.

import random

def coordenadas_soma(lista: list, valor: int) -> tuple | str:  
    n1 = n2 = 0
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] + lista[j] == valor and lista[i] != lista[j]:
                n1 = lista[i]
                n2 = lista[j]
                return n1, n2
    return "Par não encontrado"

def coordenadas_otima_soma(lista: list, valor: int) -> tuple:
    complementos = {}

    for n in range(len(lista)):
        try:
            if (complementos[lista[n]]):
                return (n, complementos[lista[n]])
        except Exception:
            complementos[valor - lista[n]] = n
    raise Exception("Pares não localizados")

def lista_aleatoria() -> list:
    lista = []
    for i in range(random.randint(1, 100)):
        lista[i] = random.randint(1, 10)
    return lista

escolha = int(input("Valor: "))
numeros = [5, 2, 3, 1, 6, 7]
soma_10 = coordenadas_soma(numeros, escolha)

print(soma_10)
