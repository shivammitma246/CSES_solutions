n=int(input())
arr1=set()
arr2=set()
if (((n)*(n+1))/2)%2!=0:
    print("NO")
elif n%2==0:
    half=n//2
    print("YES")
    for i in range(1,half+1):

        if i%2==0:
            arr1.add(i)
            arr1.add(n-i+1)
        else:
            arr2.add(i)
            arr2.add(n - i + 1)
    print(len(arr1))
    for i in arr1:
        print(i,end=" ")
    print(len(arr2))
    for i in arr2:
        print(i,end=" ")
else:
    arr1.add(1)
    arr1.add(2)
    arr2.add(3)
    print("YES")
    for i in range(4,4+(n+1-4)//2):
        if i%2==0:
            arr1.add(i)
            arr1.add(n-i+4)
        else:
            arr2.add(i)
            arr2.add(n - i + 4)
    print(len(arr1))
    for i in arr1:
        print(i,end=" ")
    print("")
    print(len(arr2))
    for i in arr2:
        print(i,end=" ")
