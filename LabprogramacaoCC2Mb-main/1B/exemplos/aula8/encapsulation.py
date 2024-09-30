class ContaErro(Exception):
  pass

class Conta:
  def __init__(self, saldo_inicial):
    self.__saldo = saldo_inicial

  def sacar(self, valor):
    if self.__saldo > valor:
      self.__saldo -= valor
    else:
      raise ContaErro('Saldo Insuficiente.')

  def depositar(self, valor):
    self.__saldo += valor

  def consultar_saldo(self):
    return self.__saldo

  def transferir(self, destino, valor):
    self.sacar(valor)
    destino.depositar(valor)


conta = Conta(100)
outra_conta = Conta(200)

try:
  conta.transferir(outra_conta, 101)
except ContaErro as ce:
  print(ce)

print('Saldo da conta 1: ', conta.consultar_saldo())
print('Saldo da conta 2: ', outra_conta.consultar_saldo())