for i in range(1, int(input("Enter The Height of The Triangle  ")) + 1):
    print(int((10 ** i - 1) / 9) ** 2)
    
------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------------------------------
n = int(input("Enter The height of the triangle you want  "))
for row in range(1, (n + 1)):
    line = ""
    for column in range(1, (row + 1)):
        line = line + str(column)
    for x in range(int(line[-1])):
        line = line + str(int(line[-1]) - 1)
    print(int(line) // 10)
