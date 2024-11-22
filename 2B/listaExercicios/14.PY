'''
14. Crie um array de tamanho 15 contendo números inteiros aleatórios entre 0 e
100. Use máscaras para:
a. Selecionar todos os números pares.
b. Substituir os números ímpares por -1.
'''
import numpy as np

arr = np.random.randint(0, 100, 15)
print(arr[arr % 2 == 0])
arr[arr % 2 != 0] = -1
print(arr)