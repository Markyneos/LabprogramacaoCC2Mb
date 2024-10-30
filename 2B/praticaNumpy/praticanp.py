import numpy as np
import matplotlib.pyplot as plt

temperaturas = np.random.randint(15, 35, size=30)

print(temperaturas)

#Calcule a temperatura média do mês

print(f"{np.mean(temperaturas):.2f}°C")

#Identifique a temperatura mais e mais baixa

menor = temperaturas.min()
maior = temperaturas.max()
print(f"Menor: {menor} | Maior: {maior}")

#Calcule a mediana das temperaturas

print(np.median(temperaturas))

#Manipulação de Dados
#Apresentar uma lista contendo apenas as ocorrências de temperatura iguais ou acima de 30°C.

maioresDe30 = temperaturas[temperaturas >= 30]
print(maioresDe30)
print(temperaturas[temperaturas >= 30])

#Crie uma nova lista das temperaturas na escala Fahrenheit
#tf = (tc * 9 / 5) + 32

fahrenheit = (temperaturas * 9 / 5) + 32
print(temperaturas)
print(fahrenheit)

#Gráfico das temperaturas

plt.plot(temperaturas, marker='o')
plt.title('Temperaturas diárias ao longo do mês')
plt.xlabel("Dia")
plt.ylabel("Temperatura (°C)")
plt.show()

#Divida as temperaturas em 4 sets que equivalem às 4 semanas de um mês

semanas = np.array_split(temperaturas, 4)
print(semanas)

mediasSemanais = [np.mean(semana) for semana in semanas]
print(mediasSemanais)

plt.bar(range(1, 5), mediasSemanais, color=['red', 'blue', 'yellow', 'green'])
plt.title("Média das Temperaturas")
plt.xlabel("Semana")
plt.ylabel("Temperatura Média(°C)")
plt.xticks(range(1, 5), ['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4'])
plt.show()
