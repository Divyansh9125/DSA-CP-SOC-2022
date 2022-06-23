from math import sqrt
def isPrime(x):
 
    if (x <= 1):
        return False
 
    # Check from 2 to sqrt(n)
    for i in range(2, int(sqrt(x))+1):
        if (x % i == 0):
            return False
    return True

n= int(input())
for k in range (n):
    A = list(map(int,input().split()))
    B = []
    for j in range(len(A)):
        if isPrime(A[j]):
            B.append(A[j])
        B = B
    p = max(B)
    print(p)