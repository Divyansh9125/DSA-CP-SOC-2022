x,y = map(int,input().split())
if (x<0 ^ y<0):
    sign = -1
else:
    sign = 1

x = abs(x)
y = abs(y)
ans = 0
while(x>=y):
    x = x-y
    ans = ans +1

if sign == -1:
    ans = -ans
else:
    ans = ans

print(ans)