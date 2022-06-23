from math import ceil


stack = list(map(int,input().split()))
n = len(stack)
index_of_mid = ceil((n+1)/2) - 1
stack2 = []
for i in range (n-1,index_of_mid,-1):
    stack2.append(stack[i])
    stack.pop()
stack.pop()
length = len(stack2)
for i in range (length-1,-1,-1):
    stack.append(stack2[i])
    stack2.pop()

print(stack)


