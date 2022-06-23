n,m = map(int,input().split())
A = list(map(int,input().split()[:n]))
B = list(map(int,input().split()[:m]))
for i in range (m):
    for j in range (n):
        if (B[i] == A[j]):
            print(A[j])
            break
        elif (B[i] > A[j]):
            print (A[j])
            break
        else:
            print
            
