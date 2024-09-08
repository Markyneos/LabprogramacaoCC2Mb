#Função que somará as vezes que 'x' ou 'o' apareceram nas linhas do tabuleiro,
# a fim de definir a vitória de algum jogador
def soma_linhas(matriz, jogador):
  soma2 = 0
  soma = []
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      if matriz[i][j] == jogador:
          soma2 += 1
    soma.append(soma2)
    soma2 = 0
  return soma

#Função que somará as vezes que 'x' ou 'o' apareceram nas colunas do tabuleiro,
# a fim de definir a vitória de algum jogador
def soma_colunas(matriz, jogador):
  soma = []
  soma2 = 0
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      if matriz[j][i] == jogador:
        soma2 += 1
    soma.append(soma2)
    soma2 = 0
  return soma

#Função para somar a quantidade de vezes que 'x' ou 'o' aparecem na
# a primeira diagonal do tabuleiro, a fim de verificar a vitória dos jogadores
def soma_diagonal(tabuleiro, jogador):
  soma = 0
  for i in range(len(tabuleiro)):
    for j in range(len(tabuleiro[i])):
      if tabuleiro[i][j] == jogador and i == j:
        soma += 1
  return soma

#Função para somar a quantidade de vezes que 'x' ou 'o' aparecem na
# a primeira diagonal do tabuleiro, a fim de verificar a vitória dos jogadores
def soma_diagonal2(tabuleiro, jogador):
    soma = 0
    if tabuleiro[0][2] == jogador:
        soma += 1
    if tabuleiro[1][1] == jogador:
        soma += 1
    if tabuleiro[2][0] == jogador:
        soma += 1
    return soma
