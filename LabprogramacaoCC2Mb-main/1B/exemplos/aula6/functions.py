def minha_funcao(**kwargs):
  print(f"Meu nome é {kwargs['nome']}")
  print(f"Meu sobrenome é: {kwargs['sobrenome']}")
  print(f"Minha idade é: {kwargs['idade']}")

minha_funcao(nome="Wagner", sobrenome="Perin", idade=39, sexo="M")

def soma(v1=0, v2=0):
  return v1 + v2

def multiplica(v1=0, v2=0):
  resultado = 0
  for i in range(v2):
    resultado = soma(resultado, v1)

  return resultado



print(f"A soma deu: {soma(5, 5)}")
print(f"A multiplicação deu: {multiplica(3, 5)}")

