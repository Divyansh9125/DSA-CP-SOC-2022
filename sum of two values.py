n,x = map(int,input().split())
A = list(map(int,input().split()[:n]))
def sumofval(arr,res):
    arr.sort()
    low = 0
    high = len(arr) - 1
    while (low < high):
        if (arr[low] + arr[high] == res):
            print(low,high)
            return
        if(arr[low] + arr[high] > res):
            high = high - 1
        else:
            low = low + 1
    
    print ("impossible")

sumofval(A,x)


