# n = int(input("Digite um número inteiro: "))
def n_primos(n):
  quantidadePrimos = 0
  while (n > 0):
    divisor = n
    quantidadeDeDivisores = 0
    while divisor > 0 :
      if (n % divisor == 0):
        quantidadeDeDivisores += 1
      divisor = divisor - 1
    numeroEPrimo = quantidadeDeDivisores == 2
    if numeroEPrimo:
      quantidadePrimos += 1
    n -= 1
  return quantidadePrimos
# print(n_primos(n))