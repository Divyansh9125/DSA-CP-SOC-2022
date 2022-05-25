n = int(input())
a = []
b = []
for i in range(n):
    strng = input().split()
    a.append(int(strng[0]))
    b.append(int(strng[1]))
a.sort()
b.sort()
count = 0
maxcount = 0
i = 0
j = 0
while(i<n and j<n):
    if a[i]>b[j]:
        j+=1
        count = count-1
    elif a[i]<b[j]:
        i+=1
        count = count+1
        maxcount = max(maxcount, count)
    else:
        i+=1
        j+=1
print(maxcount)
