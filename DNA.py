dna=input()
max=0
leng=0
i=0
while i<len(dna):
    flag=0
    leng = 0
    j=i
    while j<len(dna) and j+1<len(dna) and  dna[j] == dna[j + 1]:

        leng=leng+1
        j=j+1
        flag=1
        if leng>max:
            max=leng

    i=i+leng+1

print(max+1)
