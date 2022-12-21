# lista = [2, 4, 2, 2, 3, 3, 1]
def remove_repetidos(lista):
  novaLista = []
  for element in lista:
    if (element in novaLista):
      print('')
    else:
      novaLista.append(element)
  novaLista.sort()
  return novaLista
# print(remove_repetidos(lista))