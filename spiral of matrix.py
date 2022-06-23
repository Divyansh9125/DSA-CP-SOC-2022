import numpy as np
n,m = map(int,input().split())
entries = list(map(int, input().split()))
a = np.array(entries).reshape(n,m)

def printSpiral(mat,R,C):
    top = 0
    left = 0
    bottom = R - 1
    right = C - 1

    while(top <= bottom and left <= right):
        for i in range (left,right+1):
            print(mat[top][i])
            top = top + 1
        
	    for i in range (top,bottom+1):
            print(mat[i][right])
            right = right - 1

		if(top <= bottom):
            for i in range (right,left+1):
                print(mat[bottom][i])
                bottom = bottom - 1

		if(left <= right):
            for i in range (bottom,top+1):
                print(mat[i][left])
                left = left + 1

printSpiral(a,n,m)