n,m = map(int,input().split())
def factorial(a):
    if (a==0 or a==1):
        return 1
    else:
        return (a * factorial(a - 1))

print(factorial(n + m -1) / (factorial(m) * factorial(n - 1)))