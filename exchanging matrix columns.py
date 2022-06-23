import numpy as np
n,m = map(int,input().split())
entries = list(map(int, input().split()))
a = np.array(entries).reshape(n,m)

for i in range (n):
    a[i][0],a[i][m-1] = a[i][m-1],a[i][0]

print(a) 