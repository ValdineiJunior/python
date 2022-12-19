def maior_primo(x):
  def ePrimo(k):
    counter = 0
    divisor = k
    while (divisor >= 1):
      if (x % divisor == 0):
        counter = counter + 1
      divisor = divisor - 1
    if (counter <= 2):
      return True
    if (counter > 2):
      return False
  teste = True
  while (teste):
    if (ePrimo(x)):
      teste = False
    else:
      x = x - 1
  return x
