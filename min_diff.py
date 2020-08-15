n =input()
something= map(int, input().split())
num_list=list(something)
n=len(num_list)
sum=sum(num_list)
min=9223372036854775807
for i in range(1<<n):
        s=bin(i)[2:]
        s='0'*(n-len(s))+s
        sum1 = 0
        for i in range(len(s)):
            if s[i]=='1':
                sum1=sum1+num_list[i]
        if abs(sum-2*sum1)<min:
            min=abs(sum-2*sum1)
print(min)