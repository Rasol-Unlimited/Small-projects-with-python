def is_prime(x):

  if x <= 1:
    return False
  elif x <= 3:
    return True
  elif x % 2 == 0 or x % 3 == 0:
    return False

  i = 5
  while i * i <= x:
    if x % i == 0 or x % (i + 2) == 0:
      return False
    i += 6

  return True

def prime_factors(x):

  factors = []
  divisor = 2
  while x > 1:
    # taqsim bar kochik tarin adad haye aval (2, 3, 5, ...)
    while x % divisor == 0:
      factors.append(divisor)
      x //= divisor  # taqsiam adad
    divisor += 1 if divisor == 2 else 2

  return factors

x = int(input("yek adad sahih mosbat vared konid: "))

if x <= 0:
  print("Error: lotfan yek adad sahih mosbat vared konid.")
else:

  prime_factors_list = prime_factors(x)


  if prime_factors_list:
    print(f"tashkil shode az {x}: {prime_factors_list}")
  else:
    print(f"{x} yek adad aval mibashad")