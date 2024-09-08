import csv

students = [
  {'nome': 'Nathan', 'idade': 18, 'naturalidade': 'São Paulo'},
  {'nome': 'Nicolas', 'idade': 32, 'naturalidade': 'Xique Xique'},
  {'nome': 'Maria', 'idade': 18, 'naturalidade': 'Vitória'},
  {'nome': 'Gabriel', 'idade': 26, 'naturalidade': 'Vitória'},
  {'nome': 'Kaiky', 'idade': 18, 'naturalidade': 'Vitória da Conquista'}
]

file_name = 'students.csv'

with open(file_name, mode='w', newline='') as file:
  writer = csv.DictWriter(file, fieldnames=['nome', 'idade', 'naturalidade'])
  writer.writeheader()
  writer.writerows(students)

print(f'O Arquivo {file_name} foi criado com sucesso!')