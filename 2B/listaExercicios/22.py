'''
22.Crie um array com os valores x=[0,π/2,π,3π/2,2π]. Calcule o seno e o
cosseno de cada valor.
'''
import numpy as np

x = np.array([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi])
seno = np.sin(x)
cosseno = np.cos(x)
print(x)
print(seno)
print(cosseno)
