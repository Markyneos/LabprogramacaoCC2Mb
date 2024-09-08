def print_matrix(mat):
  for row in mat:
    print(" ".join(str(n) for n in row))
mat = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

print_matrix(mat)

'''print("PELO ÍNDICE")
for i in range(len(mat)):
  for j in range(len(mat)):
    print(mat[i][j])

print("SEM O ÍNDICE")
for row in mat:
  for n in row:
    print(n)
'''