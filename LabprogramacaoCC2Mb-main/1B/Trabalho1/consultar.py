import csv


def consultar():
  file_name = 'dados.csv'

  #Recebe o nome do cadastro para exibir seus dados
  nome = input("Digite um nome para procurar seus dados: ")
  resultados = []
  
  #Lê o arquivo .csv e armazena os resultados da pesquisa em uma lista
  with open(file_name, mode = 'r') as file:
    reader = csv.DictReader(file)
    for linha in reader:
      if linha['nome'] == nome:
        resultados.append(linha)

    #Caso não tenha achado nenhum resultado, retorna ao menu, e, caso contrário, exibe seus dados
    if resultados == []:
      print("Não foi encontrado nenhum resultado!")
    else:
      for resultado in resultados:
        resultado['idade'] = int(resultado['idade'])
        resultado['cpf'] = int(resultado['cpf'])
        print(f"Nome: {resultado['nome']} || Idade: {resultado['idade']} || CPF: {resultado['cpf']} || Senha: {resultado['senha']}")