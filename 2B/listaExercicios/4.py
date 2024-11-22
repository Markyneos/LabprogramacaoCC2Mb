'''
4. Crie um array de 20 números aleatórios entre 0 e 1. Calcule a média, o
desvio padrão, o valor máximo e o mínimo desse array.
'''
import numpy as np

arr = np.random.randint(0, 10, 20)
#Pra ter certeza que não errei, vou fazer com um array de 0s e 1s, também, desculpa, professor, não tinha certeza
#Se vc escreveu certo.
arr2 = np.random.randint(0, 1, 20)
media = arr.mean()
media2 = arr2.mean()
desvioPadrao = np.std(arr, mean=media)
desvioPadrao2 = np.std(arr2, mean=media2)
maximo = arr.max()
maximo2 = arr2.max()
minimo = arr.min()
minimo2 = arr2.min()
print(arr)
print(arr2)
print(media)
print(media2)
print(desvioPadrao)
print(desvioPadrao2)
print(minimo)
print(minimo2)
print(maximo)
print(maximo2)
