n = int(input())
arr = input().split()
arr = [int(arr[i]) for i in range(n)]
i=0
arr.sort()
count = 0
for i in range(n-1):
    if arr[i]!=arr[i+1]:
        count+=1
print(count+1)