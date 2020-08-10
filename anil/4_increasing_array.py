n = int(input())
arr = list(map(int, input().split(" ")[:n]))
turn = 0
for i in range(len(arr)-1):
    if arr[i] > arr[i + 1]:
        turn += arr[i] - arr[i+1]
        arr[i+1] = arr[i]
print(turn)
