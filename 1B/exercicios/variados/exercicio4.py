'''
1) Crie uma função chamada "divisao_segura" que receba dois números como argumentos, 
calcule e retorne a divisão deles.
Caso o divisor seja 0, emita uma mensagem de erro.
2) Escreva uma função chamada "calculo_salario" que aceite o salário base de um
funcionário, um bônus opcional (com valor padrão 0, e um número variável de deduções.
A função deve calcular e retornar o salário final de um funcionário.
'''
def divisao_segura(n1, n2):
  if n2 != 0:
    return n1 / n2
  else:
    raise Exception("Não é possível dividir por zero!")
def calculo_salario(salario, deduct, bonus=0.0):
  total = salario - deduct
  if bonus != 0:
    total += bonus
  return total

numero1 = int(input())
numero2 = int(input())
salario = float(input("Digite seu salário: "))
deduct = float(input("Digite a dedução do seu salário: "))
confirmacao = input("Você recebe bônus?(Y/N): ")
bonus = 0
if confirmacao == 'y':
  bonus = float(input())
  print(calculo_salario(salario, deduct, bonus))

else:
  print(calculo_salario(salario, deduct))