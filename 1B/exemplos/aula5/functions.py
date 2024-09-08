'''
Funções - São blocos de instruções que podem ser executados quando chamados.
* Podem receber dados necessários para processamento (parâmetros/argumentos)
* Podem devolver valores resultantes de sua operação
'''

def minha_func():
  print("Você chamou sua função! :D")

minha_func()


def imprime_mensagem(nome):
  print(f"Olá, {nome}! Tudo bem?")

nome = input("Qual é o seu nome?: ")
imprime_mensagem(nome)

def imprime_nome_completo(nome, sobrenome="Pessoa"):
  print(f"Nome comlpeto: {nome} {sobrenome}")

imprime_nome_completo("Marco")

#Tuplas como argumentos
def minha_funcao(*args):
  print("Argumento 2: " + args[4])

try:
  minha_funcao("Arg 1", "Arg 2", "Arg 3", "Arg 4")

except:
  print("Deu erro aqui vish")

