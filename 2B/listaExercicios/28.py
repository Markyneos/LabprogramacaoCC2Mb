'''
28. Dado o array x=[0,1,2,3,4] e y=[1,2,0,2,1], crie novos valores para xxx em
passos de 0.1 usando numpy.interp. Plote os valores interpolados (se
necessário, use Matplotlib para exibir).
'''
import numpy as np
from matplotlib import pyplot

x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 2, 0, 2, 1])

xxx = np.arange(0, 4.1, 0.1)
yyy = np.interp(xxx, x, y)

pyplot.plot(x, y, 'o', label="Pontos Originais")
pyplot.plot(xxx, yyy, '-', label="Interpolação")
pyplot.xlabel('x')
pyplot.xlabel('y')
pyplot.title("Interpolação")
pyplot.show()
