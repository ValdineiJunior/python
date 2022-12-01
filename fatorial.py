n = int(input("Digite o valor de n: "))
fatorial = 1

while n > 1:
  fatorial = fatorial * n
  n = n - 1
print(fatorial)