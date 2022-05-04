n = int(input())
if n==1:
    print(1)
elif n<4:
    print("NO SOLUTION")
elif n == 4:
    print("3 1 4 2")
elif n%2 == 0:
    for i in range(n//2):
        print(i+1, end=" ")
        print(i+1+n//2, end=" ")
else:
    for i in range(n//2):
        print(i+1, end=" ")
        print(i+2+n//2, end=" ")
    print(n//2+1)