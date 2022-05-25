n = int(input())
a = []
b = []
lim = 1000000007
for i in range(n):
    s = input().split()
    a.append(int(s[0])%(lim))
    b.append(int(s[1]))
for i in range(n):
    res = 1
    while(b[i]>0):
        if b[i]&1:
            res = res*a[i]%(lim)
        a[i] = a[i]*a[i]%(lim)
        b[i] = b[i]>>1
    print(res)