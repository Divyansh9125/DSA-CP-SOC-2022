a = list(map(int,input().split()))
x = max(a)
b = set(a)
if (len(b)==1):
    y = x
else:
    b.remove(max(b))
    y = max(b)
        
print(x)
print(y)