n = int(input())
def factorial(a):
    if (a==0 or a==1):
        return 1
    else:
        return (a*factorial(a-1))

N = factorial(n)
count = 0
while (N%10 == 0):
    count+=1
    N = N/10
    
print(count)