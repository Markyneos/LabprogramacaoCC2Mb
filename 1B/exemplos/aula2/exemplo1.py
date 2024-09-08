#Escopo de variáveis
#Global

x = "Wagner"

def func():
  x = "Carlos"
  print("Meu nome é: " + x)
def func2():
  print("Meu nome é: " + x)

func()
func2()

print("Meu nome é: " + x)