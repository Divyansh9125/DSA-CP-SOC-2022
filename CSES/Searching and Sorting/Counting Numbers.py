n = int(input())
arr = input().split()
arr = [int(arr[i]) for i in range(n)]
loc = [0 for i in range(n)]
for i in range(n):
    loc[arr[i]-1]=i
count = 1
for i in range(1,n):
    if loc[i]<loc[i-1]:
        count+=1
print(count)