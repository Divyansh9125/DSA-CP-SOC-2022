a,b = map(int,input().split())
res = a + b
def bin(n):
    s = []
    while (n!=0):
        if (n%2==0):
            s.append(0)
            n = n // 2 
        else:
            s.append(1)
            n = n // 2 
      

    l = len(s)
    for i in range(l):
        s[i]==s[l-i-1]
    
    print(s)

print(bin(res))
