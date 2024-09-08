import csv


def listar():
  file_name = 'dados.csv'

  with open(file_name, mode = 'r') as file:
    reader = csv.DictReader(file)
    dados = list(reader) #[d for d in reader]
  print("Aqui estão os dados no arquivo: ")
  for dado in dados:
    print(f"Nome: {dado['nome']} || Idade: {dado['idade']} || CPF: {dado['cpf']} || Senha: {dado['senha']}")
