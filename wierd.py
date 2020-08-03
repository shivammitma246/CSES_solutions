def weird(num):
    while True:
        print(num)
        if num==1:
            break
        elif num%2==0:
            num=num/2
        else:
            num=3*num+1

if __name__ == "__main__":
    num=int(input("Enter the number : "))
    weird(num)