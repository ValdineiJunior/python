list = []
def invertendoSequencia():
  numero = int(input("Digite um número: "))
  if (numero == 0):
    for element in range((len(list)-1),-1,-1):
      print(list[element])
  else:
    list.append(numero)
    invertendoSequencia()
invertendoSequencia()