import numpy as  np
n = int(input())
entries = list(map(int, input().split()))
a = np.array(entries).reshape(n,n)
def sumuppertria(a1,n1):
    sum1 = 0
    for j in range (n1):
        for i in range (n1):
            while (i<=j):
                sum1 = sum1 +  (a1[i][j])
    print(sum1)

def sumlowertria(a2,n2):
    sum2 = 0
    for j in range (n2):
        for i in range (n2):
            while (i>=j):
                sum2 = sum2 +  (a2[i][j])
    print(sum2)

print(sumuppertria(a,n))
print(sumlowertria(a,n))