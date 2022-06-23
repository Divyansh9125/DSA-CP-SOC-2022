n = int(input())
a = list(map(int,input().split()[:n]))
for i in range(n):
    if(a[i]==1 or a[i]==2 or a[i]==3):
        print(a[i])