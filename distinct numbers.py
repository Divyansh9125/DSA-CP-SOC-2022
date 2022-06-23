n = int(input())
A = list(map(int,input().split()[:n]))
A.sort()
B = []
B.append(A[0])
for i in range (1,n):
    if (A[i] != A[i-1]):
        B.append(A[i])

print(len(B))