'''
Construa uma função que recebe uma lista de números e um n.
A função deve retornar lista2 lista com os n números maiores da lista
'''

def n_max(n, lista):
    lista2 = list(lista)
    for _ in range(len(lista2) - n):
        menor = lista2[0]
        for j in range(len(lista2)):
            if menor > lista2[j]:
                menor = lista2[j]
        for j in range(len(lista2)):
            if lista2[j] == menor:
                lista2.pop(j)
                break
    return lista2
                
    



print(n_max(3, [15, 21, 30, 20, 75, 52, 31]))