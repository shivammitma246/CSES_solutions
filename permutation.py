num = int(input())
arr=[0]*num
if num==1:
    print(1)
elif num>=4:
    for i in range(2,num,2):
        print(i,end=" ")
    if num%2==0:
        print(num, end=" ")
    for i in range(1,num,2):
        print(i,end=" ")
    if num%2!=0:
        print(num, end=" ")

else:
    print("NO SOLUTION")



