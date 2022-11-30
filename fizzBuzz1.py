numero = int(input("Digite um numero inteiro: "))

numeroEDivisivelPortres = numero % 3 == 0

if numeroEDivisivelPortres:
  print("Fizz")
else:
  print(numero)