stng = input().split()
n = int(stng[0])
x = int(stng[1])
a = input().split()
a = [int(a[i]) for i in range(n)]
arr = [int(a[i]) for i in range(n)]
a.sort()
i = 0
j = n-1
while(j>i):
    if a[i]+a[j]==x:
        break
    elif a[i]+a[j]>x:
        j-=1
    else:
        i+=1
if j>i:
    if a[i]!=a[j]:
        print(str(arr.index(a[i])+1)+" "+str(arr.index(a[j])+1))
    else:
        print(str(arr.index(a[i])+1)+" "+str(arr.index(a[j], arr.index(a[i])+1)+1))
else:
    print("IMPOSSIBLE")