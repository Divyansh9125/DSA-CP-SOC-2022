n,k = map(int,input().split())
A = list(map(int,input().split()[:n]))
i = 0
window_size = k
moving_medians = []
  
while (i < n - k + 1):
    window = A[i : i + k]
    window.sort()
    window_median = window[window_size//2]
    moving_medians.append(window_median)
    i = i + 1

print(moving_medians)
