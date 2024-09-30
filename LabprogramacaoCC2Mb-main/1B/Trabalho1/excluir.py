import csv


def excluir():
  #Recebe o nome do cadastro a ser excluído
  nome = input("Digite o nome do cadastro que você deseja excluir: ")
  file_name = 'dados.csv'
  resultado = []
  erase = []

  #Lê o arquivo .csv, e atribui o cadastro com o nome escolhido a uma lista, e o resto a outra
  with open(file_name, mode='r') as file:
    reader = csv.DictReader(file)
    for linha in reader:
      if linha['nome'] != nome:
        resultado.append(linha)
      elif linha['nome'] == nome:
        erase.append(linha)
  #Caso nenhum cadastro com o nome escolhido tenha sido achado, retorna isso para o usuário
  if erase == []:
    print("Não foi achado nenhum cadastro com esse nome!")
  #Caso contrário, cria um novo arquivo com os cadastros que não foram escolhidos
  else:
    with open(file_name, mode = 'w', newline = '') as file:
      writer = csv.DictWriter(file, fieldnames = ['nome', 'idade', 'cpf', 'senha'])
      writer.writeheader()
      writer.writerows(resultado)
    print(f"O cadastro com nome {nome} foi excluído com sucesso!")
    