import csv


def listar():
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
    print("Aqui estão os dados no arquivo: ")
    for dado in dados:
      dado['idade'] = int(dado['idade'])
      print(f"Nome: {dado['nome']} || Idade: {dado['idade']} || CPF: {dado['cpf']} || Senha: {dado['senha']}")
