n = int(input())
if n*(n+1)%4!=0:
    print("NO")
elif n%4==0:
    print("YES")
    print(n//2)
    for i in range(1,n+1,4):
        print(i, end = " ")
    for i in range(4,n+1,4):
        print(i, end = " ")
    print()
    print(n//2)
    for i in range(2,n+1,4):
        print(i, end = " ")
    for i in range(3,n+1,4):
        print(i, end = " ")
else:
    print("YES")
    print((n-3)//2+2)
    print("1 2", end = " ")
    for i in range(n,3,-4):
        print(i, end = " ")
    for i in range(n-3,3,-4):
        print(i, end = " ")
    print()
    print((n-3)//2+1)
    print("3", end = " ")
    for i in range(n-1,3,-4):
        print(i, end = " ")
    for i in range(n-2, 3,-4):
        print(i, end = " ")