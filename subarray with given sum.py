n = int(input())
a = list(map(int,input().split()[:n]))
givensum = int(input())

def findsubarr(a,n,givensum):
    b = []
    count = 0
    pre_sum = 0
    
    for i in range (n):
        pre_sum += a[i]
        if pre_sum==givensum:
           count = count + 1
        if (pre_sum - givensum) in b:
            count = count + 1
        if (a[i]==givensum):
            count = count + 1
        b.append(a[i])
    return count

print(findsubarr(a,n,givensum))