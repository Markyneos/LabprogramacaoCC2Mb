import numpy as np

l1 = np.arange(4)
l2 = np.arange(4)

l = np.concatenate((l1, l2))

print(l)

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

# l1 = np.array([1, 2, 3])
# l2 = np.array([4, 5, 6])
# l = np.concatenate(l1, l2)

#split

lista = np.arange(5)

explode = np.array_split(lista, 3)
print(explode)
