i = j = s = 0
n = 5
while i <= n:
    while j < 2 * n:
        s += 1
        j += 1
    if i % 2 == 0:
        j = i //2
    else:
        j //= 2
    print(i, j, s)
    i += 1