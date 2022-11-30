numero = int(input("Digite um numero inteiro: "))

numeroEDivisivelPorCinco = numero % 5 == 0

if numeroEDivisivelPorCinco:
  print("Buzz")
else:
  print(numero)