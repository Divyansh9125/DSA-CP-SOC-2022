m = 1000000007
n = int(input())
for i in range (n):
    a,b,c = map(int,input().split())
    print((a**(b**c))%m)