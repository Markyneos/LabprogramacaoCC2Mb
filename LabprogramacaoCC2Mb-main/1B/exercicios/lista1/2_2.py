def e_matriz_identidade(matriz):
  num_linhas = len(matriz)

  if not all(len(linha) == num_linhas for linha in matriz):
      return False

  for i in range(num_linhas):
      for j in range(len(matriz[i])):
          if i == j:
              if matriz[i][j] != 1:
                  return False
          else:
              if matriz[i][j] != 0:
                  return False

  return True

matriz = [[1, 0, 0], [0, 0, 1], [0, 0, 1]]
print(e_matriz_identidade(matriz))
