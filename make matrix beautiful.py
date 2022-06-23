import numpy as np
n = int(input())
entries = list(map(int, input().split()))
a = np.array(entries).reshape(n,n)

def findMinOpeartion(matrix, n):
 
    sumRow = [0] * n
    sumCol = [0] * n

    for i in range(n):
        for j in range(n) :
            sumRow[i] += matrix[i][j]
            sumCol[j] += matrix[i][j]
 
    maxSum = 0
    for i in range(n) :
        maxSum = max(maxSum, sumRow[i])
        maxSum = max(maxSum, sumCol[i])
 
    count = 0
    i = 0
    j = 0
    while i < n and j < n :
 
        diff = min(maxSum - sumRow[i],
                   maxSum - sumCol[j])
 
        matrix[i][j] += diff
        sumRow[i] += diff
        sumCol[j] += diff
 
        count += diff
 
        if (sumRow[i] == maxSum):
            i += 1
        if (sumCol[j] == maxSum):
            j += 1
             
    return count

print(findMinOpeartion(a,n))