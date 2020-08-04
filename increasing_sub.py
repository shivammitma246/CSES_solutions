n = int(input())
arr=list(map(int,input().split()))[:n]
summ=0
for i in range(len(arr)):
    if i==0:
        pass
    else:
        if arr[i]>=arr[i-1]:
            pass
        else:
            
            summ=summ+arr[i-1]-arr[i]
            arr[i]=arr[i-1]
print(summ)