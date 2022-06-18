seq=input()
maxcount = 0
count = 0
for i in range(1,len(seq)):
    if seq[i-1]==seq[i]:
        count = count+1
    else:
        maxcount = max(maxcount, count+1)
        count = 0
print(max(maxcount,count+1))