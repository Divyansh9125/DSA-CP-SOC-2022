arr = list(map(int,input().split()))
n = len(arr)
stack = []
length = len(stack)
curr_min = arr[0]

#pushing to the stack
for i in range (n):
    if arr[i] > curr_min:
        stack.append(arr[i])
    else:
        stack.append(2*arr[i] - curr_min)
        curr_min = arr[i]

arr.clear() 
print(curr_min)
#popping out of the stack and returning the min
for j in range (length-1,-1,-1):
    if stack[j] > curr_min:
        arr.append(curr_min)
    else:
        arr.append(curr_min)
        curr_min = 2*curr_min - arr[j]

print(curr_min)



    

    