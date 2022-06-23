def countsubarr(A,x,n):
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

    return count   

n = int(input())
B = list(map(int,input().split()[:n]))
summation = sum(B)
m = summation//n

for l in range (n,n*m,n):
    c = countsubarr(B,l,n)

print(c)

