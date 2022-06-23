n = int(input())
arr = list(map(int,input().split()[:n]))
dep = list(map(int,input().split()[:n]))
def maxcustomers(ent,exit,m):
    ent.sort()
    exit.sort()
    customers_in = 1
    max_customers = 1
    i = 1
    j = 0
    while(i<m and j<m):
        if (ent[i] <= exit[j]):
            customers_in += 1
            max_customers = max(max_customers,customers_in)
            i = i+1

        else:
            customers_in -= 1
            j = j-1
    
    print(max_customers)

maxcustomers(arr,dep,n)
