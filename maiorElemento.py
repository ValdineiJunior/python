# lista = [1,5,7,8,2,5]
def maior_elemento(lista):
  maiorElemento = lista [0]
  for elemento in lista:
    if (elemento > maiorElemento):
      maiorElemento = elemento
  return maiorElemento
# maior_elemento(lista)