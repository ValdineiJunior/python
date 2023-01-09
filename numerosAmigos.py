number1 = int(input("digite um numero: "))
number2 = int(input("digite outro numero: "))

def sumFatorial(number):
  divisor = 1
  soma = 0
  while divisor < number:
    if (number % divisor == 0):
      soma = soma + divisor
    divisor = divisor + 1
  print(soma)
  return soma
    
result1 = sumFatorial(number1)
result2 = sumFatorial(number2)
result = result1 == number2 and result2 == number1
print(result)