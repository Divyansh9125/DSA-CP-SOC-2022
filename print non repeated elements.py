n = int(input())
for i in range (n):
    a = list(map(int,input().split()[:n]))
    d = dict()
    for j in range(n):
        if a[j] in d:
            d[a[j]] += 1 
        else:
            d[a[j]] = 1
    count = 0
    for ele in d:
        if (d[ele]==1):
            print(ele,"")