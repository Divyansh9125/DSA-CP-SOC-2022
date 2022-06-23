n = int(input())
A = list(map(int,input().split()[:n]))
def printPrevSmaller(arr, n):
 
    print(0,end="")
 
    
    for i in range(1, n ):
        for j in range(i-1 ,-2 ,-1):
         
            if (arr[j] < arr[i]):
             
                print(j+1 ,", ",
                            end="")
                break
 
        if (j == -1):
            print(0,end="")

printPrevSmaller(A,n)
        