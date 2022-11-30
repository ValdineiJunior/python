import math
numero1 = int(input("Digite um numero inteiro: "))
numero2 = int(input("Digite um numero inteiro: "))
numero3 = int(input("Digite um numero inteiro: "))
numero4 = int(input("Digite um numero inteiro: "))

distancia = math.sqrt(((numero1-numero2)**2) + ((numero3-numero4)**2))

if distancia >= 10:
  print("longe")
else:
  print("perto")