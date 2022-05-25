n = int(input())
arr = input().split()
arr = [int(arr[i]) for i in range(n)]
arr.sort()
if n%2==0:
    med = (arr[n//2]+arr[n//2-1])//2
else:
    med = (arr[n//2])
x = 0
for i in range(n):
    x += abs(med-arr[i])
print(x)