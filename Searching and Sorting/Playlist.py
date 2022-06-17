n = int(input())
stng = input().split()
arr = [int(stng[i]) for i in range(n)]
i = 0
j = 0
maxseq = 1
pres = [0 for i in range(n)]
pres[arr[0]-1]+=1
while j<n-1:
    j+=1
    pres[arr[j]-1]+=1
    if pres[arr[j]-1]<=1:
        maxseq = max(maxseq, j-i+1)
    else:
        while arr[i]!=arr[j]:
            pres[arr[i]-1]-=1
            i+=1
        pres[arr[i]-1]-=1
        i+=1
print(maxseq)
