def is_prime(x):

  for i in range(2,x):
    if x % i == 0:
      return False
   return True  

if is_prime(x):
  print(f"{x} adad aval mibashad")
else:
  print(f"{x} adad aval nmibashad. maqsoam alayih: {i}")
