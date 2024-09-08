def is_on_list(list, item):
  count = 0
  for element in list:
    count += 1
    if element == item:
      print(f'Rodou {count} vezes.')
      return True

  print(f'Rodou {count} vezes.')
  return False  


students = ['Carlos', 'Maria', 'João', 'Pedro']

print(is_on_list(students, 'Nathan'))