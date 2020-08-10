n = int(input())
zeros = 0
curr = 5
while True:
    flr = n // curr
    if flr > 0:
        zeros += flr
        curr = curr * 5
    else:
        print(zeros)
        break
