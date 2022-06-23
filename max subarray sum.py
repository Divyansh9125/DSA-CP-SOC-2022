n = int(input())
A = list(map(int,input().split()[:n]))

def maxsumsubarr(s,x):
    res = s[0]
    maxend = s[0]
    for i in range (1,x):
        maxend = max(maxend + s[i], s[i])
        res = max(maxend,res)
    
    print(res)

maxsumsubarr(A,n)