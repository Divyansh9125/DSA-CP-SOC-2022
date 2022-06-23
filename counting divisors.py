n = int(input())
for i in range (n):
    x = int(input())
    count = 0
    for j in range (2,x-1):
        
        if (x%j == 0):
            count+=1
        count = count

    print (count+2)
