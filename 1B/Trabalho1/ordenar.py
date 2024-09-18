import csv


def ordenar():
  #Nome do arquivo .csv
  file_name = 'dados.csv'

  #Função que lê o arquivo .csv
  with open(file_name, mode = 'r') as file:
    reader = csv.DictReader(file)
    #Atribui os dados lidos a uma lista
    dados = list(reader) #[d for d in reader]
  #Verifica se o arquivo contem algum cadastro, caso tiver, imprimir seus dados
  if len(dados) < 1:
    print("Não há nenhum cadastro salvo!")
  else:
    while True:
      print("Por qual dado você deseja cadastrar?")
      print("1.Nome\n2.Idade\n3.CPF\n0.Voltar")
      escolha = input("Escolha: ")
      match escolha:
        case "1":
          dados = sorted(dados, key=lambda d: d['nome'])
          for dado in dados:
            print(f"Nome: {dado['nome']} || Idade: {dado['idade']} || CPF: {dado['cpf']} || Senha: {dado['senha']}")
        case "2":
          for dado in dados:
            dado['idade'] = int(dado['idade'])
          dados = sorted(dados, key=lambda d: d['idade'])
          for dado in dados:
            print(f"Nome: {dado['nome']} || Idade: {dado['idade']} || CPF: {dado['cpf']} || Senha: {dado['senha']}")
        case "3":
          dados = sorted(dados, key=lambda d: d['cpf'])
          for dado in dados:
            print(f"Nome: {dado['nome']} || Idade: {dado['idade']} || CPF: {dado['cpf']} || Senha: {dado['senha']}")
        case "0":
          break
        case _:
          print("Entrada Inválida")
