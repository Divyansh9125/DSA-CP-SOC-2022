arr = input().split()
n = int(arr[0])
x = int(arr[1])
arr = input().split()
arr = [int(arr[i]) for i in range(n)]
a = []
b = []
for i in range(x):
    stng = input().split()
    a.append(int(stng[0]))
    b.append(int(stng[1]))
loc = [0 for i in range(n)]
for i in range(n):
    loc[arr[i]-1]=i
count = 1
for i in range(1,n):
    if loc[i]<loc[i-1]:
        count+=1
for i in range(x):
    add1 = 0
    add2 = 0
    temp1 = arr[a[i]-1]
    temp2 = arr[b[i]-1]
    arr[a[i]-1] = temp2
    arr[b[i]-1] = temp1
    if abs(temp1-temp2)==1:
        for j in range(max(temp1-2, 0), min(temp2+1, n), 1):
            if j!=n-1 and loc[j]>loc[j+1]:
                add1+=1
    else:
        for j in range(max(temp1-2, 0), min(temp1, n), 1):
            if j!=n-1 and loc[j]>loc[j+1]:
                add1+=1
        for j in range(max(temp2-2, 0), min(temp2, n), 1):
            if j!=n-1 and loc[j]>loc[j+1]:
                add1+=1
    swap = loc[temp1-1]
    loc[temp1-1] = loc[temp2-1]
    loc[temp2-1] = swap
    if abs(temp1-temp2)==1:
        for j in range(max(temp1-2, 0), min(temp2+1, n), 1):
            if j!=n-1 and loc[j]>loc[j+1]:
                add2+=1
    else:
        for j in range(max(temp1-2, 0), min(temp1, n), 1):
            if j!=n-1 and loc[j]>loc[j+1]:
                add2+=1
        for j in range(max(temp2-2, 0), min(temp2, n), 1):
            if j!=n-1 and loc[j]>loc[j+1]:
                add2+=1
    count+=add2-add1
    print(count)