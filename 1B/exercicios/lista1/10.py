def e_matriz_simetrica(matriz):
  linhas = []
  colunas = []
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      linhas.append(matriz[i][j])
      colunas.append(matriz[j][i])
  return linhas == colunas

matriz = [[1, 2, 3],
          [2, 4, 5],
          [3, 5, 6]]
print(e_matriz_simetrica(matriz))