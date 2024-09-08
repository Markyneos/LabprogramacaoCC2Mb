import csv


def cadastrar():
  #Armazena os dados de inputs
  dados = [
    {'nome': input("Digite seu nome: "),
     'idade': int(input("Digite sua idade: ")), 
     'cpf': int(input("Digite seu cpf(somente números): ")),
    'senha': input("Digite sua senha: ")}
  ]
  #Nome do arquivo que será salvo os dados
  file_name = 'dados.csv'
  #Função que interage com o arquivo .CSV (neste caso, que acrescenta os dados)
  with open(file_name, mode = 'a', newline = '') as file:
    writer = csv.DictWriter(file, fieldnames=['nome', 'idade', 'cpf', 'senha'])
    writer.writerows(dados)
  #Retorna uma mensagem ao usuário
  print("Seu cadastro foi concluído com sucesso!")