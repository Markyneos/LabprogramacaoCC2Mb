def e_matriz_nula(matriz):
  resultado = True
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      if matriz[i][j] != 0:
        resultado = False
        return resultado
  return resultado

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(e_matriz_nula(matriz))