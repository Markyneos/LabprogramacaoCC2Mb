'''
12. Use numpy.linspace para criar um array com 50 valores igualmente
espaçados entre 0 e 10. Use numpy.arange para criar um array com
valores de 0 a 10, incrementando de 0.2
'''
import numpy as np

arr = np.linspace(0, 10, 50)
print(arr)
arr2 = np.arange(0, 10, 0.2)
print(arr2)