def fatorial(numero):
  resultado = numero
  while numero != 0:
    resultado *= numero - 1
    numero -= 1
  return resultado
numero = int(input("Insira um número para descobrir seu fatorial: "))
resultado = fatorial(numero)
print(resultado)