import numpy as  np
n1,m1 = map(int,input().split())
entries1 = list(map(int, input().split()))
entries2 = list(map(int, input().split()))
a = np.array(entries1).reshape(n1, m1)
b = np.array(entries2).reshape(n1, m1)

for i in range(n1):
    for j in range(m1):
        print(a[i][j] + b[i][j])
