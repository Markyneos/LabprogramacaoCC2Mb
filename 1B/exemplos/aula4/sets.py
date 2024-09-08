'''
Sets - É uma coleção não-ordenada, não-indexada e não-duplicada.
'''

frutas = {"pera", "banana", "morango"}

print(frutas)
print(type(frutas))

coisa = {"wagner", "sandra", True, 2, 1}
print(coisa)

for c in coisa:
  print(c)

print("wagner" in coisa)

coisa.add("novo_elemento")
for c in coisa:
  print(c)

minhas_compras = {"carne", "cerveja", "carvao"}
compras_alheias = {"shampoo", "condicionador", "creme"}

minhas_compras.update(compras_alheias)

for item in minhas_compras:
  print(item)

minhas_compras.remove("creme")

for item in minhas_compras:
  print(item)

# CONJUNTOS
alunos_gp1 = {"andre", "carlos", "antonio", "jose", "joao"}
alunos_gp2 = {"clara", "andre", "joao", "pedro"}

# alunos_gp = alunos_gp1.union(alunos_gp2)
alunos_gp = alunos_gp1 | alunos_gp2

print(alunos_gp)

#aluno_2grupos = alunos_gp1.intersection(alunos_gp2)
aluno_2grupos = alunos_gp1 & alunos_gp2
print(aluno_2grupos)

#diferenca = alunos_gp1.difference(alunos_gp2)
diferenca = alunos_gp1 - alunos_gp2

print(diferenca)

#diferenca_simetrica = alunos_gp1.symmetric_difference(alunos_gp2)
diferenca_simetrica = alunos_gp1 ^ alunos_gp2
print(diferenca_simetrica)