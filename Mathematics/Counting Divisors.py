n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

prime = [i for i in range(2,1001)]
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

for i in range(n):
    j = 0
    while arr[i]>1:
        if j>=len(prime):
            exp[len(exp)-1]=1
            break
        if arr[i]%prime[j]!=0:
            j = j+1
            continue
        arr[i]= arr[i]//prime[j]
        exp[j]+=1
    prod = 1
    for j in range(len(exp)):
        prod*=(exp[j]+1)
    print(prod)
    exp = [0 for i in range(len(prime)+1)]