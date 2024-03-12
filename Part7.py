import math

def newton_raphson(n, tolerance=1e-5):
  def f(x):
    return x**2 - n

  def f_prime(x):
    return 2 * x

  x0 = n
  while abs(f(x0)) > tolerance:
    x1 = x0 - f(x0) / f_prime(x0)
    x0 = x1

  return x0

n = int(input("yek adad sahih mosbat vared konid: "))
sqrt_n = newton_raphson(n)

print(f"jazr dovom {n} Newton-Raphson: {sqrt_n}")
print(f"jazr dovom {n} ba method sqrt libery math: {math.sqrt(n)}")