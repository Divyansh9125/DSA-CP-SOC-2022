def factorial (x):
    if (x==0 or x==1):
        return 1
    else:
        return (x * factorial(x-1))
        
from collections import defaultdict
A = list(map(str,input().split()))
n = len(A)
freq = [0]* 26
for i in range (n):
    if (A[i] >= 'a') :
            freq[(ord)(A[i]) - 97] = freq[(ord)(A[i]) - 97] + 1
fact = 1
for j in range (26):
    fact = fact * factorial(freq[j])

print(factorial(n) // fact)
