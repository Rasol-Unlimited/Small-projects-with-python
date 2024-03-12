import math

def stirling_approximation(n):

  return math.sqrt(2 * math.pi * n) * (n / math.e) ** n

def main():

  while True:
    try:
      n = int(input("yek adid sahih mosbat vared konid: "))
      if n <= 0:
        print("Error: yek adid sahih mosbat vared konid.")
      else:
        factorial = math.factorial(n)
        approximation = stirling_approximation(n)
        ratio = factorial / approximation
        print(f"{n}! / S({n}) = {ratio:.10f}")
        break
    except ValueError:
      print("Error: yek adid sahih mosbat vared konid.")

if __name__ == "__main__":
  main()