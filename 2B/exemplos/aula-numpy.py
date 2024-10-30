import numpy as np

listaNormal = [5, 3, 2, 8, 9]
array = np.array(listaNormal)
print(listaNormal)
print(type(listaNormal))

print(array)
print(type(array))
print(array.dtype)

#Dimensions

ar1 = np.array(42)
print(ar1)
print(ar1.ndim)

ar2 = np.array([1, 2, 3])
print(ar2)
print(ar2.ndim)

ar3 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(ar3)
print(ar3.ndim)

ar4 = np.array([1, 2, 3], ndmin=5)
print(ar4)

#index

ar = np.array([1, 2, 3])
print(ar[1])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr)
print(arr[1, 2])

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[1, 1, 1])

#Slicing

lista = np.arange(15)
print(lista)

pedaco = lista[5:9].copy()
print(pedaco)

pedaco[0] = 69
print(pedaco)
print(lista)

pedaco2 = lista[-5:]
print(pedaco2)

#Data types

frutas = np.array(('Banana', 'Maçã', 'Morango', 'Laranja'))
print(frutas)
print(frutas.dtype)
print("\U0001F600")

numeros = np.array([1, 2, 3, 4], dtype='i8')
print(numeros)
print(numeros.dtype)

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')
print(newarr)

