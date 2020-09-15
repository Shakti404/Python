from array import *

arr = array('i', [])
arr1 = array('i', [])
n = int(input("Enter The Length Of The Array "))
for i in range(n):
    x = int(input("Enter Value To The Array "))
    arr.append(x)
    if i == 2:
        pass
    else:
        arr1.append(x)
print(arr)
print(arr1)
