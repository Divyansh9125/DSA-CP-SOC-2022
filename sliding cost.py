n = int(input())
k = int(input())
A = list(map(int,input().split()[:n]))
i = 0

sliding_cost = []
  
while (i < n - k + 1):
    window = A[i : i + k]
    window_cost = max(window) - min(window)

    sliding_cost.append(window_cost)
      
    i = i + 1
  
print(sliding_cost)