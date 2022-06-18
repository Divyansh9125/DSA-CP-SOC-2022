n = int(input())
count = 0
t = 5
while n>=t:
    count = count + n//t
    t = t*5
print(count)