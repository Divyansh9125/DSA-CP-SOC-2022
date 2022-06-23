n,k = map(int,input().split())
A = list(map(int,input().split()))

count = 0   
for j in range(1,n+1):
    for l in range (len(A)):
        if (j%A[l]==0):
            count = count + 1
            break
    count = count

print(count)