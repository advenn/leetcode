from icecream import ic

x = int("1101", 2)
y = int("1010", 2)
z = x | y
ic(x, y, z, bin(x), bin(y), bin(z))

a = 3
s = 3 << 2
ic(a, s)

t = 64

ic(t >> 6)

n = int("10110", 2)
print(n)
