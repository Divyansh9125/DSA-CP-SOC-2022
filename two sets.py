n = int(input())
if (n==1):
    print("NO")
elif (n==2):
    print("YES")
    print (1)
    print(1)
    print(1)
    print(1)
elif (n==3):
    print("YES")
    print(2)
    print("2 1")
    print(1)
    print(3)

else:
    if (n%2==0):
        if (n%4!=0):
            print("NO")
        else:
            A =[]
            B =[]
            for i in range(int(n/4) -1):
                c = n-i
                d = n/2 + 1 + i
                A.append(c)
                A.append(i+1)
                B.append(d)
                B.append(n/2 - i)
           
            print("YES")
            print(len(A))
            print(A)
            print(len(B))
            print(B)

    else:
        A = []
        B = []
        if ((n-3)%4==0):
            for k in range (int((n-3)/4) -1):
                e = n-k
                f = n-(k+((n-3)/4 + 1))
                g = (n+1)/2
                A.append(e)
                A.append(k+1)
                A.append(g)
                A.append(g/2)
                B.append(f)
                B.append(k+((n-3)/4 + 2))
                B.append(g + g/2)
            
        print("YES")
        print(len(A))
        print(A)
        print(len(B))
        print(B)

        





            



