'''
Listas em Python - São ordenados, são indexados, são modificáveis, permitem duplicatas
'''

nomes = ["Wagner", "Antonio", "Jose", "Joao", "Wagner"]

print(nomes)

print(nomes[2])
nomes[2] = "Maria"
print(nomes[2])

dados = ["Nicolas", 20, 1.86, True]
print(dados)

print(len(nomes))

print(type(nomes))
print(type(nomes[2]))

print(nomes[2:])

print(nomes[2:4])

print(nomes[-1])

#in operator

if "Maria" in nomes:
  print('Eu conheço a Maria!')
else:
  print('Eu não conheço a Maria')
  print(nomes.__contains__("Maria"))

nomes = ["Wagner", "Antonio", "Jose", "Joao", "Wagner"]

#nomes[2:4] = ["Maria", "Clara", "Fernanda"]

nomes.append("Maria")

nomes.insert(2, "Fernanda")

nomes.remove("Wagner")
print(nomes)
removido = nomes.pop()
print(nomes)
print(removido)

del nomes[1]
print(nomes)
nomes.clear()
print(nomes)