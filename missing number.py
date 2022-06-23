def getMissingNo(P):
    N = len(P)
    total = (N + 1)*(N + 2)/2
    sum_of_P = sum(P)
    return total - sum_of_P

n = int(input())
A = list(map(int, input().split()[:n]))
p = getMissingNo(A)
print(int(p))


 
 
