def fatorial_r(n):
  resultado = n
  while(n > 1):
    n = n - 1
    resultado = resultado * n
  return resultado

def fatorial(n):
  if(n > 1):
    return n * fatorial(n - 1)
  else:
    return 1

def arranjo(n, p):
  return fatorial(n) / fatorial(n - p)

def combinacao(n, p):
  return fatorial(n) / (fatorial(p) * fatorial(n - p))

print(f"O fatorial de 5 é: {fatorial(5)}")
print(f"O arranjo de 5, 2 a 2 é: {arranjo(5, 2)}")
print(f"A combinação de 5, 2 a 2 é: {combinacao(5, 2)}")