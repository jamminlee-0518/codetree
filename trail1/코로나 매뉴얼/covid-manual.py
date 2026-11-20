a_c, a_t = map(str, input().split())
b_c, b_t = map(str, input().split())
c_c, c_t = map(str, input().split())
list = [a_c, b_c, c_c, c_t, b_t, a_t]
em = 0
for i in range(1, 5):
    if list[i-1] == "Y" and int(list[-i]) >= 37:
        em += 1
if em >= 2:
    print("E")
else:
    print("N")