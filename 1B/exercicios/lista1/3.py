def extrair_diagonal(matriz):
  diagonal = []
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      if i == j:
        diagonal.append(matriz[i][j])

  return diagonal

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(extrair_diagonal(matriz))