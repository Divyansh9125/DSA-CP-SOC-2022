def sumofdiv(x):
    
    divisors = [1]
    for j in range(2,x+1):
        if (x%j == 0):
            divisors.append(j)
    return sum(divisors)

n = int(input())
s  = 0
for i in range (1,n+1):
    s = s + sumofdiv(i)
    
print(s)




