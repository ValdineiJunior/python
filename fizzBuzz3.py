numero = int(input("Digite um numero inteiro: "))

numeroEDivisivelPorTres = numero % 3 == 0
numeroEDivisivelPorCinco = numero % 5 == 0
numeroEDivisivelPorTresEPorCinco = numeroEDivisivelPorTres and numeroEDivisivelPorCinco
if numeroEDivisivelPorTresEPorCinco:
  print("FizzBuzz")
else:
  print(numero) 