strng = input().split()
n = int(strng[0])
m = int(strng[1])
h = input().split()
h = [int(h[i]) for i in range(n)]
h.sort()
t = input().split()
t = [int(t[i]) for i in range(m)]
for i in range(m):
    lb = 0
    ub = len(h)-1
    while(lb<=ub):
        mid = (lb+ub)//2
        if t[i]==h[mid]:
            ind = mid
            break
        elif t[i]>h[mid]:
            lb = mid+1
        else:
            ub = mid-1
    if t[i]<h[mid]:
        mid = mid-1
    if mid==-1:
        print(-1)
    else:
        print(h[mid])