n = int(input())
ls = [[int(i) for i in input().split()] for j in range(n)]
for l, r in ls:
    if l > r:
        l = l + r
        r = l - r
        l = l - r
    if 2 * l < r:
        print("NO")
    elif 2 * l == r:
        print("YES")
    else:
        l = l % 3
        r = r % 3
        if l == 0 and r == 0:
            print("YES")
        elif (l == 1 and r == 2) or (l == 2 and r == 1):
            print("YES")
        else:
            print("NO")
