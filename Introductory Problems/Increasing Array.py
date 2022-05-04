input()
num = input().split()
count = 0
num[0] = int(num[0])
for i in range(1, len(num)):
    num[i] = int(num[i])
    if num[i-1]>num[i]:
        count = count + num[i-1] - num[i]
        num[i] = num[i-1]
print(count)