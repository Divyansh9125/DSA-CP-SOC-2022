q = int(input())
k = []
for i in range(q):
    k.append(int(input()))
for i in range(q):
    t = 0
    while k[i]-9*(10**(t-1))*t >0:
        if t!=0:
            k[i] = k[i] - 9*(10**(t-1))*t
        t = t+1
    num = int(k[i]-1)//(t)
    rem = int(k[i]-1)%(t)
    res = str(10**(t-1)+num)
    print(res[rem])

