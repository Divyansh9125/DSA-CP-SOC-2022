def comp(arr, n, t):
    


n = int(input())
if n*(n+1)%4!=0:
    print("NO")
else:
    t = n*(n+1)//4
    arr = []
    arr = comp(arr, n, t)