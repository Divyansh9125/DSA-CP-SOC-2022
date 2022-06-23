n = int(input())
a = list(map(str,input().split()[:n]))
d = dict()
for j in range(n):
    if a[j] in d:
        d[a[j]] += 1 
    else:
        d[a[j]] = 1

maxx = 1
winner = ""
for ele in d:
    val = d[ele]
    if (val>maxx):
        maxx = val
        winner = ele
    elif (val==maxx and winner>ele):
        winner = ele

print (winner)
