s = str(input())
s = list(s)
n = len(s)
stack = [0]

def push(stack,ele):
    stack.append(ele)

def top(stack):
    length = len(stack)
    return stack[length-1]

def pop(stack):
    stack.pop()

for i in range(n):
    if (s[i] == top(stack)):
        pop(stack)
    else:
        push(stack,s[i])

stack.remove(0)
string = str(stack)
print(string)

