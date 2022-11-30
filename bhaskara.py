import math
numeroA = int(input("Digite um numero inteiro: "))
numeroB = int(input("Digite um numero inteiro: "))
numeroC = int(input("Digite um numero inteiro: "))

delta = (numeroB ** 2) - (4 * numeroA * numeroC)

if delta < 0:
  print("esta equação não possui raízes reais")
else:
  if delta == 0:
    raiz = ((math.sqrt(delta)) - numeroB) / (2 * numeroA)
    print("a raiz desta equação é",raiz)
  else:
    raiz1 = ((math.sqrt(delta)) - numeroB) / (2 * numeroA)
    raiz2 = (-(math.sqrt(delta)) - numeroB) / (2 * numeroA)
    if raiz1 < raiz2:
      print("as raízes da equação são",raiz1,"e",raiz2)
    else:
      print("as raízes da equação são",raiz2,"e",raiz1)