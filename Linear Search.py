# from array import *
# import numpy

pos = -1


def Find(list, num):
    i = 0
    while i < len(list):
        if list[i] == num:
            globals()['pos'] = i
            return True
        i += 1
    else:
        return False


my_list = []
n = int(input("Enter The Length Of The Array "))
for i in range(n):
    x = int(input("Enter Value To The Array "))
    my_list.append(x)
print(my_list)
n = int(input("Enter The Number You Want To Find "))

if Find(my_list, n):
    print("Found at", pos + 1)
else:
    print("Not Found")
