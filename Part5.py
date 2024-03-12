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

x = int(input("yek adad vared konid (x >= 2): "))

if is_prime(x):
  print(f"{x} adad aval mibashad")
else:
  
  for i in range(2, x):
    if x % i == 0:
      print(f"{x} adad aval nmibashad. maqsoam alayih: {i}")
      break