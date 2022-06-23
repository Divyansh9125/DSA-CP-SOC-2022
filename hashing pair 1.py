n = int(input())
a = list(map(int,input().split()[:n]))
x = int(input())

hashmap = {}
def findpairs(arr,size,summ):
    for i in range (size):
        temp = summ - arr[i]
        if (temp in hashmap):
            print(temp,arr[i])
        
        hashmap[arr[i]] = i
        
print(findpairs(a,n,x))