stack = list(map(int,input().split()))

def push(stack,ele):
    stack.append(ele)
    print(stack)

def pop(stack):
    stack.pop()
    print(stack)

push(stack,2)
push(stack,3)
pop(stack)


