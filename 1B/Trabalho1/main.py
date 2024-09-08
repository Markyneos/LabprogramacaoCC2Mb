from cadastrar import cadastrar
from consultar import consultar
from excluir import excluir
from listar import listar

#Menu Main
while True:
  print("O que você deseja fazer?:\n 0.Sair\n 1.Cadastrar\n 2.Listar\n 3.Consultar\n 4.Excluir")
  print("Escolha uma opção(0, 1, 2, 3 ou 4): ")
  escolha = int(input())
  match escolha:
    case 1:
      cadastrar()
    case 2:
      listar()
    case 3:
      consultar()
    case 4:
      excluir()
    case 0:
      print("Tchau!")
      break