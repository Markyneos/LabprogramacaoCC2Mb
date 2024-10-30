import numpy as np

pessoas = np.array(['Carlos', 'João', 'Carla', 'Pedro', 'Carlos']) 

x = [True, True, False, False, True]

print(pessoas)
print(pessoas[x])

print(pessoas == 'Carlos')
print(pessoas[pessoas == 'Carlos'])

#Exercício

numeros = np.array([np.random.randint(1000) for _ in range(100)])

#Imprima uma lista apenas com os números entre 100 e 200
print(numeros > 100)
