def e_matriz_esparsa(matriz):
  zeros = 0
  outro = 0
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      if matriz[i][j] == 0:
        zeros += 1
      else:
        outro += 1
  return zeros > outro

matriz1 = [[1, 2, 3], [4, 0, 0]]
matriz2 = [[0, 0, 1], [0, 0, 0]]

print(e_matriz_esparsa(matriz1))
print(e_matriz_esparsa(matriz2))