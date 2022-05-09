def div(apple, ideal, res):
    if len(apple)==0 or ideal<apple[len(apple)-1]:
        return ideal
    for i in range(len(apple)):
        if ideal-apple[i]>=0:
            res = min(div(apple[i+1:],ideal-apple[i],res), res)
    return res



n = int(input())
apple = input().split()
apple = [int(apple[i]) for i in range(len(apple))]
apple.sort(reverse=True)
res = sum(apple)
ideal = res//2
ideal = div(apple, ideal, res)
if res%2==0:
    res = 2*ideal
else:
    res = 2*ideal+1
print(res)