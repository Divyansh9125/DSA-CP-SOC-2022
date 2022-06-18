s = input()
arr = [0]*26
for i in range(len(s)):
    arr[ord(s[i])-ord('A')]+=1
count = 0
loc = -1
for i in range(26):
    if arr[i]%2==0:
        count+=1
    else:
        loc = i
if count<=24:
    print("NO SOLUTION")
else:
    ans = ""
    for i in range(26):
        for j in range(arr[i]//2):
            ans = ans + chr(ord('A')+i)
    if loc!=-1:
        ans = ans + chr(ord('A')+loc)
    for i in range(25,-1,-1):
        for j in range(arr[i]//2):
            ans = ans + chr(ord('A')+i)
    print(ans)
