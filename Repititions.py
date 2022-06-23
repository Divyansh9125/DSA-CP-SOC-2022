A = list(map(str, input().split()))
i = 0
max_length = 1
while (i+1 != len(A)):
    if (A[i] == A[i+1]):
        k=i
        while (A[i] == A[i+1]):
            i = i+1
        length = i-k+1
        max_length = max(length , max_length)
    else:
        i = i+1
    
print(max_length)
