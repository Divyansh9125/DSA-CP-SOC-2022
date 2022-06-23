s = str(input())
s = list(s)

def push(stack,ele):
    stack.append(ele)

def pop(stack):
    stack.pop()

def top(stack):
    length = len(stack)
    return stack[length-1]

def matching(a,b):
    if a=='(' and b==')' or a=='{' and b=='}' or a=='[' and b==']':
        return True
    return False

def parenthesis(s):
    n = len(s)
    stack = []
    for i in range (n):
        if (s[i]=='(' or s[i]=='{' or s[i]=='['):
            push(stack,s[i])
        else:
            if (bool(s)==True):
                return False
            elif (matching(top(stack),s[i])==False):
                return False
            else:
                pop(stack)
    
    return bool(s)==True

if parenthesis(s):
    print("true")
else:
    print("false")
            
        