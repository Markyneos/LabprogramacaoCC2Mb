'''
Dictionary Usados para armazenar pares chave->valor.
É uma coleção ordenada, modificável, não-indexada e não aceita duplicatas.
'''

carro = {
  "marca": "Ford",
  "modelo": "Mustang",
  "ano": 1964
}

print(carro)
print(type(carro))

print("O modelo do carro é " + carro["modelo"])
carro["ano"] = 1980
print(carro)

print(len(carro))

carro["cor"] = "Cinza"
print(carro)

print(carro.get("modelo"))

chaves = carro.keys()
valores = carro.values()

print(chaves)
print(valores)

items = carro.items()
print(items)

carro["cores_disponiveis"] = ["azul", "verde", "amarelo"]
print(carro)

#carro["placa"] = "MSS-2024"

if "placa" in carro:
  print("Eu sei a placa do carro!")
else:
  print("Eu não sei a placa do carro.")

#carro["ano"] = 2000

carro.update({"ano": 2000})
print(carro)

print(carro.keys())
c = carro.pop("cores_disponiveis")
print(carro.keys())
print(c)

ultima = carro.popitem()
print(carro)

del carro["ano"]

print(carro)

carro.clear()
print(carro)

del carro
#a variável não existe mais

carro = {
  "marca": "Ford",
  "modelo": "Mustang",
  "ano": 1964,
  "cor": "Cinza",
  "eletrico": False
}

for p in carro:
  print(p)

for p in carro:
  print(p + " - " + str(carro[p]))

for chave, valor in carro.items():
  print(f"{chave} - {valor}")