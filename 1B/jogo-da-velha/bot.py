import random
from somas import soma_colunas, soma_diagonal, soma_diagonal2, soma_linhas

#Inicia a definição da função do bot
def bot(tabuleiro: list) -> list:
  #Verifica se "a soma" de 'x' na primeira diagonal é igual a 2, para impedir a vitória do jogador
  if soma_diagonal(tabuleiro, 'x') == 2:
    for i in range(len(tabuleiro)):
      for j in range(len(tabuleiro[i])):
        if i == j:
          if tabuleiro[i][j] == ' ':
            tabuleiro[i][j] = 'o'
            return tabuleiro
          else:
            pass
  #Verifica se "a soma" de 'x' na segunda diagonal é igual a 2, para impedir a vitória do jogador
  if soma_diagonal2(tabuleiro, 'x') == 2:
    for i in range(len(tabuleiro)):
      if tabuleiro[i][len(tabuleiro) - 1 - i] == ' ':
        tabuleiro[i][len(tabuleiro) - 1 - i] = 'o'
        return tabuleiro
  #Verifica o número de 'x's em cada coluna do tabuleiro, para, caso o número seja 2, impedir que o jogador ganhe
  lista = soma_colunas(tabuleiro, 'x')
  for i in range(len(lista)):
    if lista[i] == 2:
      for j in range(len(lista)):
        if tabuleiro[j][i] == ' ':
          tabuleiro[j][i] = 'o'
          return tabuleiro
  #Verifica o número de 'x's em cada linha do tabuleiro, para, caso o número seja 2, impedir que o jogador ganhe
  lista2 = soma_linhas(tabuleiro, 'x')
  for i in range(len(lista2)):
    if lista2[i] == 2:
      for j in range(len(lista2)):
        if tabuleiro[i][j] == ' ':
          tabuleiro[i][j] = 'o'
          return tabuleiro
  #Caso em nenhum caso o jogador possa ganhar o jogo, ou não seja possível de impedir, o bot realiza uma jogada aleatória
  while True:
    coluna = random.randint(0, 2)
    linha = random.randint(0, 2)
    if tabuleiro[coluna][linha] == ' ':
      tabuleiro[coluna][linha] = 'o'
      return tabuleiro
