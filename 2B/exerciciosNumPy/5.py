# 5. Gere 1000 numeros aleatorios (entre 0 e 100) de uma distribuição. Utilize NumPy para calcular o histograma desses dados e exiba os resultado s em um gráfico utilizando um gráfico de barras do matplotlib.

import numpy as np
import matplotlib.pyplot as ptl

s = np.random.randint(0, 100, size=1000)
ptl.bar(s, s)
ptl.title('Histograma')
ptl.xlabel('Item')
ptl.ylabel('Value')
ptl.show()
