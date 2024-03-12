x = int(input('x: '))
low = 0
high = x + 1

while low < high:
    mid = (high + low) // 2
    if mid * mid <= x:
        low = mid + 1
    else:
        high = mid

print(low - 1)
