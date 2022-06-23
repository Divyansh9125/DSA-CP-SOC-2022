n = int(input())
a = list(map(int,input().split()[:n]))

def findsubarr(a,n):
    b = []
    pre_sum = 0
    b.append(0)
    for i in range (n):
        pre_sum += a[i]
        if pre_sum in b:
           return True
        b.append(pre_sum)
    return False

if(findsubarr(a,n)==True):
    print("yes")
else:
    print("no")
    

    