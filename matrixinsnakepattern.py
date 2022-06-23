import numpy as np
n,m = map(int,input().split())
entries = list(map(int, input().split()))
a = np.array(entries).reshape(n,m)
def printSnake(m,r,c):
	for i in range (r):
	    if(i % 2 == 0):
             for j in range (c):
                 print (m[i][j])	
        else:		
			 for j in range (c-1,0):
                 print(m[i][j])

printSnake(a,n,m)
            
				
