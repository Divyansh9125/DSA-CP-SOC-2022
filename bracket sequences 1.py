n = int(input())
def catalan(x):
    x = int(x)
    if (x==0):
        cat = 1
    else:
        cat = 0
        for i in range (x):
            cat = cat + catalan(i)* catalan (x-i-1)
             
    return cat

if (n%2 != 0):
    print(0)
else:
    print((catalan(n / 2)) % 10000007)

