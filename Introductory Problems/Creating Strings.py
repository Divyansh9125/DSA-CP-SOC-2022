from math import factorial
def scramble(l, ans):
    if len(l)==0:
        print("".join(ans))
        return
    for i in range(len(l)):
        if i!=0 and l[i]==l[i-1]:
            continue
        ans.append(l[i])
        scramble(l[:i]+l[i+1:], ans)
        ans.pop(len(ans)-1)
s_in= input()
arr = [0]*26
for i in range(len(s_in)):
    arr[ord(s_in[i])-ord('a')]+=1
s = []
n = factorial(sum(arr))
for i in range(len(arr)):
    for j in range(arr[i]):
        s.append(chr(i+ord('a')))
    n = n//factorial(arr[i])
print(n)
ans = []
scramble(s, ans)