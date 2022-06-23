n,k = map(int,input().split())
A = list(map(int,input().split()[:n]))

def find4Numbers(S, m, x):
	S.sort()
#fix the first element one by one and find the other two elements
	for i in range (m-2):
		for j in range (m-2):
			l = i + 1 #index of the first element in the remaining elements 
			r = m - 1 #index of the last element 
			while (l < r and i != j):
				if (S[i] + S[j] + S[l] + S[r] == x):
					print (S[i], "", S[j], "", S[l], "", S[r])
					break
				elif ((A[i] + A[l] + A[r]) < x):
					l = l + 1 
				else:
					r = r - 1
						
	print ("impossible")

print(find4Numbers(A,n,k))


