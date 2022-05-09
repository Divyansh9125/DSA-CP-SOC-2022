n = int(input())
count = 1
for i in range(n//30):
    count = (count*(2**30))%(10**9+7)
for i in range(n%30):
    count = count*2
count = count%(10**9+7)
print(count)