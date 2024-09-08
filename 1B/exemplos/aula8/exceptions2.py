
try:
  print(x)
  a = 10/0
except ZeroDivisionError as zde:
  print(zde)
except NameError as ne:
  print(ne)  

print('Uma mensagem qualquer')