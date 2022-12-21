largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
linhaBorda = "#"
linhaMeio = "#"
while (largura > 2):
  linhaBorda = linhaBorda + "#"
  linhaMeio = linhaMeio + " "
  largura -=1
linhaBorda = linhaBorda + "#"
linhaMeio = linhaMeio + "#"
contador = altura
while (contador > 0):
  if (altura == contador or contador == 1):
    print(linhaBorda)
  else:
    print(linhaMeio)
  contador -= 1