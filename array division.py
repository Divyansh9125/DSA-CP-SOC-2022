n,k = map(int,input().split())
A = list(map(int,input().split()[:n]))


def check(middle,array,l,s):
    count = 0
    sum = 0
    for i in range (l):
        if array[i] > middle:
            return False

        sum = sum + array[i]
        if (sum > middle):
            count = count + 1
            sum = array[i]

    count = count + 1

    if count <=s:
        return True
    return False

def arrdiv(arr,m,x):
    start = max(arr)
    end = 0
    for i in range (m):
        end += arr[i]
    
    ans = 0
    while (start <= end):
        mid = (start + end) // 2
        if (check(mid,arr,m,x)):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    
    return ans

print (arrdiv(A,n,k))