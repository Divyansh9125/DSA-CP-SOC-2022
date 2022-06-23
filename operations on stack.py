T = int(input())
    
while T :
    stack = []
        
    Q = int(input())
        
    for i in range(Q) :
        query = input().strip().split()
            
        if query[0] == "1" :
            stack.append(query[1])
                
        elif query[0] == "2" :
            if len(stack) == 0 :
                pass
            else :
                stack.pop()
        else :
            if len(stack) == 0:
                print(-1)
            else :
                print(stack[-1])
                    
    T -= 1
                