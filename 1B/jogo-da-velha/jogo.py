#Importando as funções dos outros arquivos
from mostrarTabuleiro import mostrarTabuleiro
from jogadorUm import jogadorUm
from jogadorDois import jogadorDois
from verificacao import verificacao
from bot import bot

#Tabuleiro do jogo da velha (matriz)
tabuleiro = [
  [' ', ' ', ' '],
  [' ', ' ', ' '],
  [' ', ' ', ' ']
]

#Dá início ao jogo
print("JOGO DA VELHA")

#Verifica a decisão do jogador
decisao = input("Você deseja jogar contra um bot?(y/n): ")

if decisao == 'n':
#Inicia uma 'main'
  while True:
    '''Mostra o tabuleiro inicial sem jogadas, em seguida pede para os jogadores fazerem suas jogadas, 
  o que irá se repetir até o loop while quebrar'''
    mostrarTabuleiro(tabuleiro)
    tabuleiro = jogadorUm(tabuleiro)
    mostrarTabuleiro(tabuleiro)
  
  #Verifica se alguém ganhou o jogo, e, caso sim, para o programa
    if verificacao(tabuleiro):
      break
  
    #Jogada do jogador dois
    tabuleiro = jogadorDois(tabuleiro)
  
  #Verifica se alguém ganhou o jogo, e, caso sim, para o programa
    if verificacao(tabuleiro):
      break
    
elif decisao == 'y':
  #Inicia uma 'main'
  while True:
    '''Mostra o tabuleiro inicial sem jogadas, em seguida pede para os jogadores fazerem suas jogadas, 
  o que irá se repetir até o loop while quebrar'''
    mostrarTabuleiro(tabuleiro)
    tabuleiro = jogadorUm(tabuleiro)
    
    #Verifica se alguém ganhou o jogo, e, caso sim, para o programa
    if verificacao(tabuleiro):
      mostrarTabuleiro(tabuleiro)
      break
    
    #Jogada do bot
    tabuleiro = bot(tabuleiro)
    
    #Verifica se alguém ganhou o jogo, e, caso sim, para o programa
    if verificacao(tabuleiro):
      mostrarTabuleiro(tabuleiro)
      break