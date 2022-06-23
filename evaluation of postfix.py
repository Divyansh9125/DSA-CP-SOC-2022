s = str(input())
s = list(s)
n = len(s)
stack = []
for i in range (n):
    if (s[i]>='0' and s[i]<='9'):
        stack.append(s[i])
    else:
        temp1 = stack.pop()
        stack = stack
        temp2 = stack.pop()
        if (s[i] == '+'):
            res = int(temp2) + int(temp1)
        elif (s[i] == '-'):
            res = int(temp2) - int(temp1)
        elif (s[i] == '*'):
            res = int(temp2) * int(temp1)
        else:
            res = int(temp2) / int(temp1)

        stack.append(res)

print(stack)