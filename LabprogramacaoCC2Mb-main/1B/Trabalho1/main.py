import csv
from cadastrar import cadastrar
from consultar import consultar
from excluir import excluir
from listar import listar
from pathlib import Path
from ordenar import ordenar

#Nome do arquivo .CSV
file_name = Path('dados.csv') 

#Verifica se o arquivo .csv existe, caso contrário, ele criará um novo
if file_name.is_file():
  pass
else:
  with open(file_name, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames = ['nome', 'idade', 'cpf', 'senha'])
    writer.writeheader()

#Nome do sistema
print("SISTEMA DE CADASTRO DE CLIENTES AMAZON")

#Menu Main
while True:
  print("O que você deseja fazer?:\n 0.Sair\n 1.Cadastrar\n 2.Listar\n 3.Consultar\n 4.Excluir\n 5.Ordenar")
  print("Escolha uma opção(0, 1, 2, 3, 4 ou 5): ")
  try:
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
      case 5:
        ordenar()
      case 0:
        print("Tchau!")
        break
      case _:
        print("Digite um número válido!")
  except ValueError:
    print("Digite um valor válido!")
