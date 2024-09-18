#Importando as funções dos outros arquivos
from somas import soma_colunas
from somas import soma_linhas
from somas import soma_diagonal
from somas import soma_diagonal2

def verificacao(tabuleiro: list) -> bool:
#Atribui a variáveis o número de 'pontos' dos jogadores em cada coluna
  coluna1 = soma_colunas(tabuleiro, "x")
  coluna2 = soma_colunas(tabuleiro, "o")
  
  #Atribui a variáveis o número de 'pontos' dos jogadores em cada linha
  linha1 = soma_linhas(tabuleiro, "x")
  linha2 = soma_linhas(tabuleiro, "o")
  
  #Atribui a variáveis o número de 'pontos' dos jogadores em cada uma das duas diagonais
  diagonal1 = soma_diagonal(tabuleiro, "x")
  diagonal1_2 = soma_diagonal2(tabuleiro, "x")
  diagonal2 = soma_diagonal(tabuleiro, "o")
  diagonal2_2 = soma_diagonal2(tabuleiro, "o")
  
  #Verifica se os jogadores tem a quantidade necessária de pontos para vitória:
  #Diagonais
  if diagonal1 == 3 or diagonal1_2 == 3:
    print("O jogador 1 venceu!")
    return True
  if diagonal2 == 3 or diagonal2_2 == 3:
    print("O jogador 2 venceu!")
    return True

  #Colunas e linhas (verifica-se as listas dos pontos de cada linha/diagonal)
  for i in range(len(coluna1)):
    if coluna1[i] == 3 or linha1[i] == 3:
      print("O jogador 1 venceu!")
      return True
    elif coluna2[i] == 3 or linha2[i] == 3:
      print("O jogador 2 venceu!")
      return True
      
  #Caso nenhum jogador atinja a vitória e os espaços acabem, o programa irá acabar declarando empate
  contador = 0
  for i in range(len(tabuleiro)):
    for j in range(len(tabuleiro[i])):
      if tabuleiro[i][j] == ' ':
        contador += 1
  if contador == 0:
    print("Empate!")
    return True

  return False
