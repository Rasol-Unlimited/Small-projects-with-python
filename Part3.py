def overlap(a, b, c, d):
    if (a <= d) and (c <= b):
        if (a == c) and (b == d):
            return f"fasele haye [{a}, {b}] ta [{c}, {d}] kamelan hampoushani darand."
        else:
            return f"fasele haye [{a}, {b}] ta [{c}, {d}] dar baze haye [{max(a, c)}, {min(b, d)}] hampoushi darand."
    else:
        return f"dar in favasel hlich hampushi vojod nadard. fasele bayin baze ha barabr ba {abs(c - a)} mibashad."

a = int(input("meqdar a ra baraye baze avali moshakhas konid: "))
b = int(input("meqdar b ra baraye baze avali moshakhas konid: "))
c = int(input("meqdar c ra baraye baze dovomi moshakhas konid: "))
d = int(input("meqdar d ra baraye baze dovomi moshakhas konid: "))

print(overlap(a, b, c , d))
