n = int(input("Digite um número inteiro: "))
soma = 0
ultimoDigito = 1

while n >= 1:
  ultimoDigito = n % 10
  soma = soma + ultimoDigito
  n = n // 10
print(soma)
