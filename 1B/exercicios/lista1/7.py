def soma_linhas(matriz):
  soma2 = 0
  soma = []
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      soma2 += matriz[i][j]
    soma.append(soma2)
    soma2 = 0
  return soma
def soma_colunas(matriz):
  soma = []
  soma2 = 0
  colunas = len(matriz[0])
  for i in range(colunas):
    for j in range(len(matriz)):
      soma2 += matriz[j][i]
    soma.append(soma2)
    soma2 = 0
  return soma


matriz = [[1, 2, 3, 4],
          [5, 6, 7, 8]]
print(soma_linhas(matriz))
print(soma_colunas(matriz))
