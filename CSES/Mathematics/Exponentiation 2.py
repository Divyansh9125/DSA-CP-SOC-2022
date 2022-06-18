n = int(input())
a = []
b = []
c = []
lim = 1000000007
for i in range(n):
    s = input().split()
    a.append(int(s[0])%(lim))
    b.append(int(s[1]))
    c.append(int(s[2]))
for i in range(n):
    for j in range(c[i]):
        res = 1
        cpy = b[i]
        while(cpy>0):
            if cpy&1:
                res = res*a[i]%(lim)
            a[i] = a[i]*a[i]%(lim)
            cpy = cpy>>1
        a[i] = res
    print(res)