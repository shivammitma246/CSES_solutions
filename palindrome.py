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
                for j in range(dict[i]//2):
                    string=i+string+i
    else:
        for i in dict:
            for j in range(dict[i]//2):
                string=i+string+i
print(string)
