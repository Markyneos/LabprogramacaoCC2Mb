import csv


def consultar():
  file_name = 'dados.csv'

  nome = input("Digite um nome para procurar seus dados: ")
  resultados = []
  
  with open(file_name, mode = 'r') as file:
    reader = csv.DictReader(file)
    for linha in reader:
      if linha['nome'] == nome:
        resultados.append(linha)

    if resultados == []:
      print("Não foi encontrado nenhum resultado!")
    else:
      for resultado in resultados:
        print(f"Nome: {resultado['nome']} || Idade: {resultado['idade']} || CPF: {resultado['cpf']} || Senha: {resultado['senha']}")