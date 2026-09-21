def max_consecutive_ones(arr, N):
    left = 0
    zero_count = 0
    max_len = 0
    
    for right in range(len(arr)):
        if arr[right] == 0:
            zero_count += 1
        
        while zero_count > N:
            if arr[left] == 0:
                zero_count -= 1
            left += 1
            
        max_len = max(max_len, right - left + 1)
    return max_len

# Sample Input
print(max_consecutive_ones([1,1,0,0,0,1,0,1,1], 2))

# Input 1
print(max_consecutive_ones([1 0 1 0 0 1 0 1 1 0 0 1 0 1 0 0 0 1 1 0 1 0 0 0 1 1 1 1 1 0 1 0 1 0 1 0 1 0 0 1 0 0 0 1 1 0 1 0 1 1 0 0 0 1], 3))
####### THINK HOW TO MAKE THIS INPUT ACCEPTABLE

# print(max_consecutive_ones())
# print(max_consecutive_ones())
