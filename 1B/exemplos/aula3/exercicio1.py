nomes = ['Jorge', 'Antonio', 'Fernanda', 'Jose', 'Joao', 'Wagner', 'Maria']

nomes_com_j = []
for nome in nomes:
  if "J" in nome:
    nomes_com_j.append(nome)

print("NOMES COM J: ", nomes_com_j)

#USANDO LIST COMPREHENSION

nomes_com_j = [nome for nome in nomes if nome[0] == "J"]

print("NOMES COM J: ", nomes_com_j)
