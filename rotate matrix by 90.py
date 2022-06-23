import numpy as np
n = map(int,input().split())
entries = list(map(int, input().split()))
a = np.array(entries).reshape(n,n)


for i in range(len(a)):
    a[i].reverse()
 
# make transpose of the matrix
for i in range(len(a)):
    for j in range(i, len(a)):
        # swapping mat[i][j] and mat[j][i]
        a[i][j], a[j][i] = a[j][i], a[i][j]
 

for i in range(0, len(a)):
    for j in range(0, len(a)):
        print(a[i][j], end=' ')
    print()
 