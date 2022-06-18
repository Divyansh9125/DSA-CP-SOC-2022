n = int(input())
num_list = input().split()
present = [False] * n
for i in range(n-1):
    present[int(num_list[i])-1]=True
print(present.index(False)+1)
