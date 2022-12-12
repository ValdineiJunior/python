n = int(input("Digite um número inteiro: "))
quantidadeDeDigitos = len(str(n))
ultimoDigito = n % 10
n = n // 10
saoIguais = False
while quantidadeDeDigitos > 1:
  saoIguais = ultimoDigito == n % 10
  ultimoDigito = n % 10
  n = n // 10
  if saoIguais:
    quantidadeDeDigitos = 0
  quantidadeDeDigitos -= 1
if saoIguais:
  print("sim")
else:
  print("não")
