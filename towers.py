from bisect import bisect_right
n = int(input())
A = list(map(int,input().split()[:n]))
tow = []
count = 0
for i in A:
    pos = bisect_right(tow,i)
    if pos >= count:
        tow = tow + [i]
        count += 1
    else:
        tow[pos] = i
print (count)