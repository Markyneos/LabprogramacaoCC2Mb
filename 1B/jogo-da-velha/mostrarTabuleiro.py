#Função que 'imprime' o tabuleiro no console, terminal, etc. de forma que ele esteja mais
# propenso ao jogo
def mostrarTabuleiro(tabuleiro: list):
  for row in tabuleiro:
    print("|".join(row))
