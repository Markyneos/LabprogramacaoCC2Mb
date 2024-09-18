#Função que somará as vezes que 'x' ou 'o' apareceram nas linhas do tabuleiro,
# a fim de definir a vitória de algum jogador
def soma_linhas(matriz: list, jogador: str) -> list:
    soma = []
    for i in range(len(matriz)):
        contador = 0
        for j in range(len(matriz[i])):
            if matriz[i][j] == jogador:
                contador += 1
        soma.append(contador)
    return soma

#Função que somará as vezes que 'x' ou 'o' apareceram nas colunas do tabuleiro,
# a fim de definir a vitória de algum jogador
def soma_colunas(matriz: list, jogador: str) -> list:
    soma = []
    for i in range(len(matriz[0])):  
        contador = 0
        for j in range(len(matriz)):  
            if matriz[j][i] == jogador:
                contador += 1
        soma.append(contador)
    return soma

#Função para somar a quantidade de vezes que 'x' ou 'o' aparecem na
# a primeira diagonal do tabuleiro, a fim de verificar a vitória dos jogadores
def soma_diagonal(tabuleiro: list, jogador: str) -> int:
  soma = 0
  for i in range(len(tabuleiro)):
    for j in range(len(tabuleiro[i])):
      if tabuleiro[i][j] == jogador and i == j:
        soma += 1
  return soma

#Função para somar a quantidade de vezes que 'x' ou 'o' aparecem na
# a primeira diagonal do tabuleiro, a fim de verificar a vitória dos jogadores
def soma_diagonal2(tabuleiro: list, jogador: str) -> int:
    soma = 0
    for i in range(len(tabuleiro)):
        if tabuleiro[i][len(tabuleiro) - 1 - i] == jogador:
            soma += 1
    return soma
