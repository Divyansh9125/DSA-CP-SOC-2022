n = int(input())
arr = [0,0,8]
for i in range(1,min(n+1,4)):
    print(i*i*(i*i-1)//2-arr[i-1])
if n>=4:
    count = arr[2]
    for k in range(4, n+1):
        count = count + 16 + 8*(k-4)
        print(k*k*(k*k-1)//2-count)