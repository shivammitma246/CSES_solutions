n = int(input())
arr = list(map(int, input().split(" ")[:n]))
total = (n*(n+1))//2
numSum = sum(arr)
print(total-numSum)
