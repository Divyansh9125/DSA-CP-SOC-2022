n = int(input())
for k in range(1,n+1):
    count = 0
    for i in range(k*k):
        x = i%k
        y = i//k
        if (0<=x+1<k and 0<=y+2<k):
            count = count+1
        if (0<=x+1<k and 0<=y-2<k):
            count = count+1
        if (0<=y+1<k and 0<=x+2<k):
            count = count+1
        if (0<=y+1<k and 0<=x-2<k):
            count = count+1
    count = count
    print(k*k*(k*k-1)//2-count)