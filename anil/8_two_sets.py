n = int(input())
total = int(n * (n + 1) / 2)
if total % 2 != 0:
    print("NO")
else:
    print("YES")
    a = set()
    b = set()
    sumA = 0
    sumB = 0
    for i in range(n, 0, -1):
        if sumA > sumB:
            sumB += i
            b.add(i)
        else:
            sumA += i
            a.add(i)
    print(len(a))
    print(*a)
    print(len(b))
    print(*b)
