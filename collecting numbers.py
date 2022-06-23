n = int(input())
A = list(map(int,input().split()[:n]))
count = 0
for j in range (2,n+1):
    if (A.index(j) < A.index(j-1)):
        count = count + 1
    count = count
print(count + 1)
