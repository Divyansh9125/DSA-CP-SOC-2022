t = int(input())
for i in range (t):
    a,b = map(int,input().split())
    if ((a%2==0 and b == a-1) or (b%2==0 and a == b-1)):
        print("YES")
    elif (a==b and a%2 != 0 and b%2 != 0):
        print("YES")
    else:
        print("NO")