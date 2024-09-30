#Strings

x = 'assim'
y = "Assim"

if x == y:
  print('Iguais')

if x == y.casefold():
  print('Iguais')

#Slicing

x = "Wagner Perin"

print(x[7:])
print(x[0:7])

print(x[-5:])

print(x.upper())
print(x.lower())

x = '     Wagner Perin  '

print(x)
print(x.strip())

x = "Vagner Perin"
y = x.replace("V", "W")

print(x)
print(y)

nomes = "Wagner, Carlos, André"
alunos = nomes.split(", ")

print(alunos)
print(type(alunos))

nomes = "Wagner Carlos André"
alunos = nomes.split(" ")
print(alunos)

nome = "Wagner"
sobrenome = "Perin"

nome_completo = nome + ' ' + sobrenome

print(nome_completo)

#Strings formatadas
idade = 22
nome = "Wagner Perin"

saida = f"Meu nome é {nome} e tenho {idade} anos."

print(saida)

preco = 58
produto = "Camiseta"

saida = f"O {produto} custa R${preco:.2f}"
print(saida)

#Escapes

frase = "E o Nicolas disse 'Olá, professor'."

print(frase)

frase = "E o Nicolas disse: \n \"Olá, professor\' \\"
print(frase)

#String methods:
