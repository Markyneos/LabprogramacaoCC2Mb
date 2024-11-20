import numpy as np

arquivoArray = np.genfromtxt('vendas.csv', delimiter=',', dtype=str)
valorTotal = arquivoArray[1:,5].astype(float)
precoUnitario = arquivoArray[1:,4].astype(float)
quantidadeVendida = arquivoArray[1:,3].astype(int)

result_avg_valorTotal = np.average(valorTotal)
resultMedianValorTotal = np.median(valorTotal)
resultStdValorTotal = np.std(valorTotal)
print(f'Total de vendas | Média: {result_avg_valorTotal} | Mediana: {resultMedianValorTotal} | Desvio Padrão: {resultStdValorTotal}')

produtoA = arquivoArray[1:,2] == "Produto A"
produtoB = arquivoArray[1:,2] == "Produto B"
produtoC = arquivoArray[1:,2] == "Produto C"

quantidadeVendidaProdutoA = quantidadeVendida[produtoA]
quantidadeVendidaProdutoB = quantidadeVendida[produtoB]
quantidadeVendidaProdutoC = quantidadeVendida[produtoC]

totalA = np.sum(quantidadeVendidaProdutoA)
totalB = np.sum(quantidadeVendidaProdutoB)
totalC = np.sum(quantidadeVendidaProdutoC)

totalGeral = np.array([totalA, totalB, totalC])
produtos = np.array(['Produto A', 'Produto B', 'Produto C'])
print(f'Mais vendido: {produtos[np.argmax(totalGeral)]}')

valorTotalProdutoA = valorTotal[produtoA]
valorTotalProdutoB = valorTotal[produtoB]
valorTotalProdutoC = valorTotal[produtoC]

totalA = np.sum(valorTotalProdutoA)
totalB = np.sum(valorTotalProdutoB)
totalC = np.sum(valorTotalProdutoC)

totalGeral = np.concatenate((totalA, totalB, totalC), axis=None)
produtos = np.array(['Produto A', 'Produto B', 'Produto C'])
print(f'Produto com maior valor total em vendas: {produtos[np.argmax(totalGeral)]}')

norte = arquivoArray[1:,1] == "Norte"
sul = arquivoArray[1:,1] == "Sul"
leste = arquivoArray[1:,1] == "Leste"
oeste = arquivoArray[1:,1] == "Oeste"

valorTotalNorte = valorTotal[norte]
valorTotalSul = valorTotal[sul]
valorTotalLeste = valorTotal[leste]
valorTotalOeste = valorTotal[oeste]

totalNorte = np.sum(valorTotalNorte)
totalSul = np.sum(valorTotalSul)
totalLeste = np.sum(valorTotalLeste)
totalOeste = np.sum(valorTotalOeste)
print(f"Norte: {totalNorte} / Sul: {totalSul} / Leste: {totalLeste} / Oeste: {totalOeste}")

quantidadeVendidaTotal = np.sum(quantidadeVendida)
datasUnicas = np.unique(arquivoArray[1:,0])
mediaDia = quantidadeVendidaTotal / len(datasUnicas)
print(f"Média por dia: {mediaDia}")

maior = 0
for day in datasUnicas:
    verificador = arquivoArray[1:,0] == day
    quantidadeVendidaNoDia = quantidadeVendida[verificador]
    somaDoDia = np.sum(quantidadeVendidaNoDia)
    if somaDoDia > maior:
        maior = somaDoDia
        maiorVendaDia = day

print(f'O dia com mais vendas foi: {maiorVendaDia}')

anterior = 0
diferencas = []
for day in datasUnicas:
    teste = arquivoArray[1:,0] == day
    quantidadeVendidaNoDia = quantidadeVendida[teste]
    somaDoDia = np.sum(quantidadeVendidaNoDia)
    diferenca = somaDoDia - anterior
    diferencas.append(diferenca)
    anterior = somaDoDia
diferencas = np.array(diferencas)
print(diferencas)

