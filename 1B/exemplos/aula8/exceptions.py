def getItem(list, index):
  if index < 0:
    raise Exception('Indice inválido.')
  return list[index]

students = ['Carlos', 'Maria', 'João', 'Pedro']

try:
  print(getItem(students, -1))
except Exception as e:
  print(e)

print('Um print qq')