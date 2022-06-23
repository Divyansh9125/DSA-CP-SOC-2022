def permutation(n):
 
    # for storing the resultant permutations
    ans = []
 
    if n <= 3:
        ans.append(-1)
 
    # if n is even
    if n % 2 == 0:
        i = 0
        while i <= n:
            ans.append(i)
            i += 2
        i = 1
        while i < n:
            ans.append(i)
            i += 2
 
    # if n is odd
    else:
        i = 2
        while i <= n-1:
            ans.append(i)
            i += 2
        j = 1
        while j <= n:
            ans.append(j)
            j += 2
    return ans
 
N = int(input())
print(permutation(N))