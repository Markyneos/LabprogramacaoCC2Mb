nomes = ['Antonio', 'Fernanda', 'Jose', 'Joao', 'Wagner', 'Maria']

print('###Iterando  com for'):
for nomes in nomes:
  print(nomes)

print(list(range(6)))

print('###ITERANDO PELO INDICE###')
for i in range(len(nomes)):
  print(nomes[i])

print('###iterando com while###')
i = 0
while i < len(nomes):
  print(nomes[i])
  i += 1

