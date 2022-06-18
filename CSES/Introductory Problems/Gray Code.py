n = int(input())
for i in range(2**n):
    str1 = []
    for j in range(n):
        r = 2**(n-j-1)
        str1.append(str(((i+r)%(4*r))//(2*r)))
    print("".join(str1))
