n = int(input())
if (n <= 7 and n%2 == 1) or (n >= 8 and n%2 == 0):
    print(31)
elif (n <= 6 and n%2 == 0) or (n >= 7 and n%2 == 1):
    if n == 2:
        print(28)
    else:
        print(30)