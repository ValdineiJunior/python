count = 10
while count > 0:
  numero = int(input('Digite um numero inteiro positivo: '))
  fatorial = 1
  while numero > 1:
    fatorial = numero * fatorial
    numero = numero - 1
  print(fatorial)
  count = count - 1