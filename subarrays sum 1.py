n,x = map(int,input().split())
A = list(map(int,input().split()[:n]))
count = 0
for k in range(n):
    if (A[k]==x):
        count = count + 1
    count = count

for i in range(n-1):
    sum = A[i]
    for j in range (i+1,n):
        sum = sum + A[j]
        if (sum==x):
            count  = count + 1
            break
        
    if (sum!=x):
        count = count 

print(count)   
