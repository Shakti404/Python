import math as m

for i in range(500):
    root = m.sqrt(i)
    x = int(root + 0.5) ** 2
    if x == i:
        print(i)
