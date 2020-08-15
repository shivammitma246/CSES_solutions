string=input()
dict={}
for i in string:
    if i not in dict.keys():
        dict[i]=1
    else:
        dict[i]=dict[i]+1
count=0
odd=0
for i in dict:
    if dict[i]%2!=0:
        odd=i
        count=count+1
    if count==2:
        break

string=""
if count==2:
    print("NO SOLUTION")
else:
    if count==1:
        for i in range(dict[odd]):
            string=string+odd
        for i in dict:
            if i!=odd:
                string=i*(dict[i]//2)+string+i*(dict[i]//2)
    else:
        for i in dict:
            string=i*(dict[i]//2)+string+i*(dict[i]//2)
print(string)
