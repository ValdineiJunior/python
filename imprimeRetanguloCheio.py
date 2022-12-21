largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
linha = ""
while (altura > 0):
  while (largura > 0):
    linha = linha + "#"
    largura -=1
  print(linha)
  altura -= 1