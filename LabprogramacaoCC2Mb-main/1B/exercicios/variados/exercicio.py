def imc(peso, altura):
  valor = peso / (altura * altura)
  if valor < 18.5:
    print(f"Seu IMC é abaixo do peso {valor:.2f}")
  elif valor >= 18.5 and valor < 25:
    print(f"Seu IMC é normal {valor:.2f}")
  else:
    print(f"Seu IMC é acima do peso {valor:.2f}")

peso = float(input("Qual é o seu peso?(kg): "))
altura = float(input("Qual é a sua altura?(m): "))
imc(peso, altura)