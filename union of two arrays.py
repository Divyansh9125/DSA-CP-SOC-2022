from this import d


n,m = map(int,input().split())
a = list(map(int,input().split()[:n]))
b = list(map(int,input().split()[:m]))

def union(lst1,lst2):
    return (set(lst1) | set(lst2))

print(union(a,b))