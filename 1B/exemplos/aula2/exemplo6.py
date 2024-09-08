#Booleanos(True, False)

print(10 > 9)

'''
Operadores
- Aritméticos: (+, -. *, /, %, **, //)
- Atribuição: (=, +=, -=, *=, /=)
- Comparação: (==, !=, >, <, >=, <=)
- Lógicos: (and, or, not
- Membro(in, not in)
'''
#Aritméticos
a = 7
b = 3

c = a % b #Resto

c = a ** b #Potência

c = a / b #Divisão
print(c)
#Atribuição
x = 3

x += 3 #x = x + 3

x -= 3 #x = x - 3

x *= 3 #x = x * 3

x /= 3 #x = x / 3

print(x)
#Comparação e Lógico

a = 20 > 5 and 5 < 8
print(a)

alunos = ["Carlos", 'André', 'João']

print("Carlos" in alunos)
print("Wagner" not in alunos)