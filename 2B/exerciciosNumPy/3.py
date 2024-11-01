import numpy as np
#3. Crie dois arrays de 10 elementos com numeros aleatorios. 
# Compare os arrays  e crie um novo array booleano que indique onde os elementos são iguais.

arr1 = np.random.randint(1, 10, size=10)
arr2 = np.random.randint(1, 10, size=10)
boolArr = arr1 == arr2
print(boolArr)