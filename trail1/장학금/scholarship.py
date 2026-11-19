s1, s2 = map(int, input().split())
if s1 >= 90:
    if s2 >= 95:
        print(100000)
    elif s2 >= 90:
        print(50000)
    else:
        print(0)
else:
    print(0)