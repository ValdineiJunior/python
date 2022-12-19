def fizzbuzz(numeroInteiro):
  fizz = numeroInteiro % 3 == 0
  buzz = numeroInteiro % 5 == 0
  if (fizz & buzz):
    return "FizzBuzz"
  else:
    if (fizz):
      return "Fizz"
    else:
      if (buzz):
        return "Buzz"
      else:
        return numeroInteiro