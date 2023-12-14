a = int(input())
if a == 0:
    print(-1)
elif a < 0:
    b = [i for i in range(a, (a * -1)+1)]
    s = 0
    for i in range(len(b)):
        for j in range(i, len(b)):
            if b[i] * b[j] == a:
                s += 1
    print(s)
else:
    b = [i for i in range(-1 * a, a+1)]
    s = 0
    for i in range(len(b)):
        for j in range(i, len(b)):
            if b[i] * b[j] == a:
                s += 1
    print(s)
