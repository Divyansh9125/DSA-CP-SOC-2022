def factorial(a):
    if (a == 0 or a == 1):
        return 1
    else:
        return (a * factorial(a - 1))

n = int(input())
for i in range(n):
    x,y = map(int,input().split())
    bin_coeff = factorial(x) / (factorial(y) * factorial(x - y))
    print(int(bin_coeff))