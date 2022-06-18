n = int(input())
def stack(n, loc1, loc2):
    if n==0:
        return
    stack(n-1, loc1, 6-loc1-loc2)
    print(str(loc1)+" "+str(loc2))
    stack(n-1, 6-loc1-loc2, loc2)
num = 0
for i in range(n):
    num = 2*num+1
print(num)
stack(n, 1, 3)