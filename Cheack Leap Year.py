def is_leap(year):
    leap = False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = bool(~leap)

        else:
            leap = bool(~leap)
    else:
        leap = leap

    return leap


year = int(input())
print(is_leap(year))
