def steps(A,n):
    count = 0
    for j in range (2,n+1):
        if (A.index(j) < A.index(j-1)):
            count = count + 1
        count = count
    return count + 1 

def swapPositions(list, pos1, pos2):
    list[pos1-1], list[pos2-1] = list[pos2-1], list[pos1-1]
    return list  

n,m = map(int,input().split())
B = list(map(int,input().split()[:n]))
for i in range (m):
    a,b = map(int,input().split()) 
    B = swapPositions(B,a,b)
    print(steps(B,n))
    B = swapPositions(B,a,b)

