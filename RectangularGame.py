n = int(input("No of lines to follow: "))
mx = 0
my = 0
for i in range(n):
    inp = [int(a) for a in input("Enter The Dimension Of The Array ").split()]
    if mx == 0:
        mx = inp[0]
        my = inp[1]
    else:
        mx = min(mx, inp[0])
        my = min(my, inp[1])
print(mx * my)
