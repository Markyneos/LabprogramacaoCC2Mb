
try:
  file = open('dados.txt', 'r')
  content = file.read()
  print(content)
  file.close()
except FileNotFoundError:
  print('O arquivo não foi encontrado.')

