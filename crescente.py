numero1 = int(input("Digite um numero inteiro: "))
numero2 = int(input("Digite um numero inteiro: "))
numero3 = int(input("Digite um numero inteiro: "))

estaNaOrdemCrescente = numero1 < numero2 < numero3

if estaNaOrdemCrescente:
  print("crescente")
else:
  print("não está em ordem crescente")