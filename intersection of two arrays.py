n,m = map(int,input().split())
a = list(map(int,input().split()[:n]))
b = list(map(int,input().split()[:m]))

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

print(intersection(a,b))