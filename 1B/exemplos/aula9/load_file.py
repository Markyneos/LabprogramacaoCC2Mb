import csv

file_name = 'students.csv'

with open(file_name, mode='r') as file:
  reader = csv.DictReader(file)
  students = [s for s in reader]

print('Os alunos foram carregados com sucesso!')

for student in students:
  print(student)