#1: Crie uma função que receba um inteiro como 
#parâmetro e devolva o fatorial deste numero

def fatorial(numero):
  resultado = 1
  while numero != 0:
    resultado *= numero
    numero -= 1
  return resultado

print(fatorial(int(input())))

#2: Crie as funções Arranjo e Combinação que realizam 
#a função fatorial da questão anterior para realizar seus cálculos
#Arranjo = An,p = n!/(n-p)!; Cn,p = n!/p!(n - p)!
#Os resultados devem ser retornados pelas funções

def arranjo(num1, num2):
  parte1 = fatorial(num1)
  parte2 = fatorial(num1 - num2)
  resultado = parte1 / parte2
  return resultado

def combinacao(num1, num2):
  parte1 = fatorial(num1)
  parte2 = fatorial(num2) * fatorial(num1 - num2)
  resultado = parte1 / parte2
  return resultado

print(arranjo(int(input()), int(input())))
print(combinacao(int(input()), int(input())))