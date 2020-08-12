n = int(input())
for i in range(1, n + 1):
    if i == 1:
        print(0)
    elif i == 2:
        print(6)
    elif i == 3:
        print(28)
    else:
        nC2 = ((i * i) * ((i * i) - 1)) // 2
        halfSum = 0
        half = i / 2
        left = half - 2
        halfSum += 12 + left*2*10 + left*left*8
        print(int(nC2-2*halfSum), int(2*halfSum))