num=int(input())
for i in range(num):
    num1, num2 = input().split()
    num1=int(num1)
    num2=int(num2)
    if num1>num2:
        num1=num1+num2
        num2=num1-num2
        num1=num1-num2
    if num1*2<num2:
        print("NO")
    elif num1*2==num2:
        print("YES")
    else:
        num1=num1%3
        num2=num2%3
        if num1==0 and num2==0:
            print("YES")
        elif ((num1==1 and num2==2) or (num1==2 and num2==1)):
            print("YES")
        else:
            print("NO")