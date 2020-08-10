n = int(input())
ls = [[int(i) for i in input().split()] for j in range(n)]
for y, x in ls:
    if y > x:
        if y % 2 == 0:
            print(y * y - x + 1)
        else:
            y -= 1
            print(y * y + x)
    else:
        if x % 2 == 0:
            x -= 1
            print(x * x + y)
        else:
            print(x * x - y + 1)

# x--> 1,2,9,10,25,26,49,50,81
# y--> 1,4,5,16,17,36,37,64,65
"""
x:even (inc)
x:odd (dec)
y:even (dec)
y:odd (inc)

(y,x)
(even, even) : (4,4): x_top+(4-1) 
(even, odd) : (4,3): y_top-(3-1)
(odd, even) : (3,4): x_top+(3-1)
(odd, odd) : (3,3):  y_top-(3-1)

y_top/x_top : 
x(even) --> x_top
x(odd) --> y_top

+/- : 
x(even) --> +
x(odd) --> -

x-1/y-1:
x(even) --> y-1
x(odd) --> x-1

eg:
(5,3) -> y_top-(x-1)
(2,4) -> x_top+(y-1)
"""
