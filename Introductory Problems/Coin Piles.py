t = int(input())
a = []
b = []
for i in range(t):
    str = input().split()
    a.append(int(str[0]))
    b.append(int(str[1]))
for i in range(t):
    if (2*a[i]-b[i])%3==0 and 2*a[i]-b[i]>=0 and 2*b[i]-a[i]>=0:
        print("YES")
    else:
        print("NO")