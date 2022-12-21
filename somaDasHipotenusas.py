import math
# n = int(input("Digite um número inteiro positivo: "))
def soma_hipotenusas(n):
  soma = 0 
  while (n >= 1):
    if é_hipotenusa(n):
      soma += n
    n -= 1
  return soma

def é_hipotenusa(x):
  result = False
  counter = x -1
  while (counter > 1):
    cateto = math.sqrt((x * x) - (counter * counter))
    if ((cateto // 1) == cateto):
      result = True
    counter -= 1
  return result

# print(soma_hipotenusas(n))