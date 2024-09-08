def multiplicar_escalar(matriz, escalar):
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      matriz[i][j] *= escalar
  return matriz

matriz = [[1, 2], [3, 4]]
print(multiplicar_escalar(matriz, 10))