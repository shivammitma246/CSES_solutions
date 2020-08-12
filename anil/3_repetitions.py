seq = input()
prev = 0
current = 0
for i in range(len(seq) - 1):
    if seq[i] == seq[i + 1]:
        current += 1
        if i == len(seq) - 2:
            if prev < current:
                prev = current
    else:
        if prev < current:
            prev = current
        current = 0
print(prev + 1)