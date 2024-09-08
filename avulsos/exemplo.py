precos = [500, 1500, 2000, 100, 25]

#Caso 1:
novo_preco = []
for preco in precos:
    novo_preco.append(preco * 2)
print(novo_preco)

#Caso 2:
imposto = []
for preco in precos:
    if preco > 1000:
        imposto.append(preco/2)
print(imposto)

#Exemplo com List Comprehension:
#Caso 1:
novo_preco2 = [preco * 2 for preco in precos]
print(novo_preco2)

#Caso 2:
imposto2 = [preco / 2 for preco in precos if preco > 1000]
print(imposto2)