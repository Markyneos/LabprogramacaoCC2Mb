carro = {
  "marca": "Ford",
  "modelo": "Mustang",
  "ano": 1964
}

#carro2 = carro --> mesmo carro!
#carro2 = carro.copy()
carro2 = dict(carro)

carro2["cor"] = "Cinza"

print(carro)
print(carro2)

#Dicionários alinhados

minha_familia = {
  "esposa": {
    "nome": "Thamires",
    "idade": 19
  },
  "filho": {
    "nome": "Pedro Lucas",
    "idade": 3
  }
}

print(minha_familia)
print(minha_familia["filho"])
print(minha_familia["filho"]["nome"])

print(minha_familia.items())

for membro, dados in minha_familia.items():
  print(f"{membro} - {dados['nome']} - {dados['idade']}")