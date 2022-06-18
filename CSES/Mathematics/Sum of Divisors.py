n = int(input())
prime = [i for i in range(2,1000000)]
i = 0
while prime[i]<32:
    for j in range(i+1,1001):
        if j>=len(prime):
            break
        if prime[j]%prime[i]==0:
            prime.pop(j)
            j = j-1
    i = i+1
exp = [0 for i in range(len(prime)+1)]
j = 0
num = n
while num>1:
    if j>=len(prime):
        exp[len(exp)-1]=num
        break
    if num%prime[j]!=0:
        j = j+1
        continue
    num= num//prime[j]
    exp[j]+=1
sum = 1
for i in range(len(prime)):
    sum = sum*(prime[i]**(exp[i]+1))//(prime[i]-1)
sum = sum*(1+exp[len(exp)-1])
print(sum)