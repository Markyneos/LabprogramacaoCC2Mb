#Função que inicia a jogada do primeiro jogador (x), e, caso a posição escolhida esteja vazia,
# a mesma será colocada o símbolo do jogador
def jogadorUm(tabuleiro):
  print("Jogador Um:")
  while True:
    coluna = int(input("Digite qual coluna quer jogar(0, 1 ou 2): "))
    linha = int(input("Digite qual linha quer jogar(0, 1 ou 2): "))
    
    try:
      if tabuleiro[coluna][linha] != ' ':
        print("Lugar já preenchido!")
      else:
        tabuleiro[coluna][linha] = 'x'
        return tabuleiro
    except (TypeError, IndexError):
      print("Digite somente os valores indicados!")