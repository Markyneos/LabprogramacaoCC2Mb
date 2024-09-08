def criar_matriz(linhas, colunas, valor):
  mat = [[valor for i in range(colunas)] for x in range(linhas)]
  return mat

def print_matrix(mat):
  for row in mat:
    print(" ".join(str(n) for n in row))

mat = criar_matriz(3, 4, 0)

print_matrix(mat)