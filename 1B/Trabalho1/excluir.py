import csv


def excluir():
  nome = input("Digite o nome do cadastro que você deseja excluir: ")
  file_name = 'dados.csv'
  resultado = []
  erase = []

  with open(file_name, mode='r') as file:
    reader = csv.DictReader(file)
    for linha in reader:
      if linha['nome'] != nome:
        resultado.append(linha)
      elif linha['nome'] == nome:
        erase.append(linha)
  if erase == []:
    print("Não foi achado nenhum cadastro com esse nome!")
  else:
    with open(file_name, mode = 'w', newline = '') as file:
      writer = csv.DictWriter(file, fieldnames = ['nome', 'idade', 'cpf', 'senha'])
      writer.writeheader()
      writer.writerows(resultado)
    print(f"O cadastro com nome {nome} foi excluído com sucesso!")
    