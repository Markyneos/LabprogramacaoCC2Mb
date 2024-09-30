def e_matriz_identidade(matriz):
  resultado = True
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      if (i == j and matriz[i][j] == 1) or (i != j and matriz[i][j] == 1):
        resultado = True
      else:
        resultado = False
        return resultado
      return resultado
      

matriz = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
print(e_matriz_identidade(matriz))
print(matriz[1][0])
