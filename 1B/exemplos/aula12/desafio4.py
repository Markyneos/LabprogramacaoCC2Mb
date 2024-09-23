'''
1 | 2 | 3
4 | 5 | 6
7 | 8 | 9

Crie uma função que rotacione uma matriz (N X N) em 90°

7 | 4 | 1
8 | 5 | 2
9 | 6 | 3

'''

def print_matrix(mat):
  for row in mat:
    print(" ".join(str(n) for n in row))

def roda_jequiti(matriz: list) -> list:
    matriz2 = [[j for j in range(len(matriz[i]))] for i in range(len(matriz))]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz2[i][-j] = matriz[j - 1][i]
    return matriz2


matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print_matrix(roda_jequiti(matriz))

'''
Crie uma função que receba uma string por parâmetro e retorne o tamanho máximo de uma substring que não
possui caracteres repetidos.

'abacdab' -> 4
'aweawaec' -> 4
'bbbb' -> 1
'''

def tamMax(string: str) -> int:
    caracteres = [i for i in list(string)]
    caracteres_usados = []
    i = 0
    tamanho = 0
    # caracteres = set(caracteres)
    while i != len(caracteres):
      caracteres_usados = []
      for j in range(i, len(caracteres)):
        if caracteres[j] not in caracteres_usados:
          caracteres_usados.append(caracteres[j])
        else:
          break
      if len(caracteres_usados) > tamanho:
        tamanho = len(caracteres_usados)
      i += 1
    return tamanho

str4 = "abacaxi"
str1 = "abacdab"
str2 = "aweawaec"
str3 = "bbbb"
print(tamMax(str1))
print(tamMax(str2))
print(tamMax(str3))
print(tamMax(str4))
