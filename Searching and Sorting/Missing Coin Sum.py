def check(arr, val):
    if val in arr:
        return False
    i = 0
    j = 0
    temp = arr[0]
    while arr[j]<val:
        if val==temp:
            return False
        elif val>temp:
            j+=1
            temp+=arr[j]
        else:
            i+=1
            temp-=arr[i-1]
    return True

n = int(input())
arr = input().split()
arr = [int(arr[i]) for i in range(n)]
arr.sort()
i = 1
while(True):
    if check(arr, i):
        print(i)
        break
    i+=1