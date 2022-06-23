import numpy as np
n,m = map(int,input().split())
entries = list(map(int, input().split()))
a = np.array(entries).reshape(n,m)


rez = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
print("\n")
for row in rez:
    print(row)