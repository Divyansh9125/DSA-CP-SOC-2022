strng = input().split()
n = int(strng[0])
m = int(strng[1])
k = int(strng[2])
a = input().split()
b = input().split()
for i in range(n):
    a[i] = int(a[i])
for i in range(m):
    b[i] = int(b[i])
a.sort()
b.sort()
count = 0
i = 0
j = 0
while(i<n and j<m):
    if a[i]-k<=b[j]<=a[i]+k:
        count+=1
        i+=1
        j+=1
    elif a[i]-k>b[j]:
        j+=1
    else:
        i+=1
print(count)