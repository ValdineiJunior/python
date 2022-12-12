n = int(input("Digite um número inteiro: "))
divisor = n
quantidadeDeDivisores = 0
while divisor > 0 :
  if (n % divisor == 0):
    quantidadeDeDivisores += 1
  divisor = divisor - 1
numeroEPrimo = quantidadeDeDivisores == 2
if numeroEPrimo:
  print("primo")
else:
  print("não primo")