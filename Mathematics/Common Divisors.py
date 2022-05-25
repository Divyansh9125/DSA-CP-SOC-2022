n = int(input())
arr = input().split()
arr = [int(arr[i]) for i in range(len(arr))]
arr.sort(reverse=True)
def gcd(m, n, mx):
    if mx>n:
        return 0
    if m%n==0:
        return n
    else:
        return gcd(n, m%n, mx)
max_num = 1
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if max_num>max(arr[i], arr[j]):
            continue
        max_num = max(max_num, gcd(max(arr[i], arr[j]), min(arr[i], arr[j]), max_num))
print(max_num)