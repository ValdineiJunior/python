numero = int(input("Digite um numero inteiro: "))

numeroEPar = numero % 2 == 0

if numeroEPar:
  print("par")
else:
  print("ímpar")