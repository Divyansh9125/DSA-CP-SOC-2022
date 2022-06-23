import numpy as np
n,m = map(int,input().split())
entries = list(map(int, input().split()))
a = np.array(entries).reshape(n,m)

for i in range(n):
    for j in range(m//2):
        a[i][j],a[i][m-1-j] = a[i][m-1-j],a[i][j]

print(a)