n = int(input())+1
arr = ("0 "+input()).split()
arr = [int(arr[i]) for i in range(n)]
pmin = min(arr[1:])
minind = 0
maxind = 0+1
for i in range(2,n):
    arr[i] = arr[i] + arr[i-1]
    if arr[i]>=arr[maxind]:
        maxind = i
minval = min(0, min(arr[:maxind]))
sum1 = arr[maxind]-minval

arr = [-arr[i] for i in range(n)]
minind = 0
maxind = 1
for i in range(1,n):
    if arr[i]>=arr[maxind]:
        maxind = i
minval = max(arr[:maxind])
sum2 = -(arr[maxind]-minval)
print(max(sum1, sum2, pmin))