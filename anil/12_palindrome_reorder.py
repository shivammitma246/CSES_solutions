from collections import Counter

data = input()
count = Counter(data)
if len(data) % 2 == 0:
    alleven = 0
    for element in count.values():
        if element % 2 != 0:
            break
        else:
            alleven += element // 2
    if alleven == len(data) // 2:
        result = ""
        for k, v in count.items():
            result += k * (v // 2)
        print(result + result[::-1])
    else:
        print("NO SOLUTION")
else:
    oddCount = 0
    middle = ""
    result = ""
    for k, v in count.items():
        if v % 2 != 0:
            oddCount += 1
            middle = k
        else:
            result += k*(v//2)
    if oddCount == 1:
        result += middle
        print(result+result[:len(result)-1][::-1])
    else:
        print("NO SOLUTION")

import pdb; pdb.set_trace()
print("HI")


