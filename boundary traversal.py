import numpy as np
n,m = map(int,input().split())
entries = list(map(int, input().split()))
a = np.array(entries).reshape(n,m)

def bTraversal(mat,R,C):
	if(R == 1):
		for i in range (C):
            print(mat[0][i])

	elif(C == 1):
        for i in range (R):
            print(mat[i][0])
	
	else:
        for i in range (C):
			print(mat[0][i])
		for i in range (R):
			print(mat[i][C - 1])
		for i in range (C-2,-1):
			print(mat[R - 1][i])
		for i in range (R-2,0):
			print(mat[i][0])

bTraversal(a,n,m)
