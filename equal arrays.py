n = int(input())
a = list(map(int,input().split()[:n]))
b = list(map(int,input().split()[:n]))

if (sorted(a)==sorted(b)):
    print("yes")
else:
    print("no")       