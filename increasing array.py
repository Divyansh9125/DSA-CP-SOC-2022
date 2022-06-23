n = int(input())
A = list(map(int,input().split()))
count = 0
for i in range(len(A)-1):
    while (A[i+1] < A[i]):
            A[i+1] += 1
            count += 1
    count = count
print(count)
            
