t = int(input())
for i in range (t):
    A = list(map(int,input().split()[:t]))
    B = list(map(int,input().split()[:t]))
    for j in range (t):
        for k in range (j+1,t):
            if (A[j] <= A[k] and B[j] >= B[k]):
                print (1)
                continue
    
    print (0)

    for j in range (t):
        for k in range (j+1,t):
            if (A[j] >= A[k] and B[j] <= B[k]):
                print (1)
                continue
            
    print (0)

    

    


