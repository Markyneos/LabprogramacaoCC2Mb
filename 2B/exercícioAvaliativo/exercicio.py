import numpy as np
import datetime

arquivoArray = np.loadtxt("vendas.csv", str, delimiter=",")
quantidadeVendida = arquivoArray[1:,3].astype(int)
precoU = arquivoArray[1:,4].astype(float)
valorT = arquivoArray[1:,5].astype(float)