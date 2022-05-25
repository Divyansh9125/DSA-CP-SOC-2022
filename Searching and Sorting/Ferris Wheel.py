strng = input().split()
n = int(strng[0])
x = int(strng[1])
arr = input().split()
arr = [int(arr[i]) for i in range(n)]
arr.sort()
i = 0
j = n-1
count = 0
while(i<=j):
    if i==j:
        count+=1
        break
    elif arr[i]+arr[j]<=x:
        count+=1
        i+=1
        j-=1
    else:
        count+=1
        j-=1
print(count)