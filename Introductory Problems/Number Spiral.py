t = int(input())
test = []
for i in range(t):
    coord = input().split()
    coord[0]=int(coord[0])
    coord[1]=int(coord[1])
    test.append(coord)
for i in range(t):
    x = test[i][1]
    y = test[i][0]
    n = max(x,y)-1
    if n%2==0:
        if y>x:
            print(n*n+x)
        else:
            print(n*n+n*2-y+2)
    else:
        if y<x:
            print(n*n+y)
        else:
            print(n*n+n*2-x+2)
