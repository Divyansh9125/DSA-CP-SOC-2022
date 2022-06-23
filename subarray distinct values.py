n,k = map(int,input().split())
A = list(map(int,input().split()[:n]))

def atMostK(arr, n, k):
#sliding window technique
    count = 0
    left = 0
    right = 0
    # Map to keep track of number of distinct elements in the current window
    map = {}
 
    # Loop to calculate the count
    while(right < n):
         
        if arr[right] not in map:
            map[arr[right]] = 0
 
        # Calculating the frequency of each
        # element in the current window
        map[arr[right]] += 1
 
        # Shrinking the window from left if the
        # count of distinct elements exceeds K
        while(len(map) > k):
 
            if arr[left] not in map:
                map[arr[left]] = 0
 
            map[arr[left]] -= 1
 
            if map[arr[left]] == 0:
                del map[arr[left]]
 
            left += 1
 
        # Adding the count of subarrays with at most
        # K distinct elements in the current window
        count += right - left + 1
        right += 1
 
    print(count)

atMostK(A,n,k)
