a, b, c = map(int, input().split())
n1 = (1 if a <= b and a <= c else 0)
n2 = (1 if a == b and b == c and c == a else 0)
print(n1, n2)