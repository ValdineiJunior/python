numberOne = int(input("Digite o primeiro número"))
numberTwo = int(input("Digite o segundo número"))

def maximo(numberOne,numberTwo):
  if (numberOne > numberTwo):
    return numberOne
  else:
    return numberTwo

maximo(numberOne,numberTwo)