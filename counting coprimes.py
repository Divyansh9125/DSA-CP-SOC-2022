def gcd(a,b):
    if (b == 0):
        return a
    else:
        return gcd(b,a%b)

n = int(input())
for i in range (n):
    A = list(map(int,input().split()))
    x = len(A)
    count = 0
    for j in range (x):
        for k in range (j+1,x):
            if (gcd(A[j], A[k])==1):
                count = count + 1
            count = count
    print(count)