def circle(n, k, count):
    #if n
    if (n+count)//2>=k:
        return 2*k-count
    elif n%2==0:
        return 2*circle(n//2,k-n//2, count)-1+count
    else:
        return 2*circle(n-n//2-count, k-n//2-count, (count+1)%2)-1+count
q = int(input())
n=[]
k=[]
for i in range(q):
    s = input()
    s = s.split()
    n.append(int(s[0]))
    k.append(int(s[1]))
for i in range(q):
    if n[i]==1:
        print("1")
        continue
    print(circle(n[i],k[i],0))