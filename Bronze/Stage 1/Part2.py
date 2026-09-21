def find_median(arr):
    s = sorted(arr)
    n = len(s)
    if n % 2 != 0:
        return s[n // 2]
    else:
        return (s[(n // 2) - 1] + s[n // 2]) / 2.0
# sample input 
print(find_median([3,1,4,2]))         # output: 2.5
# input 1
print(find_median([5, 2, 8, 9, 1, 4, 7, 3, 6, 10]))         # output: 5.5
# input 2
print(find_median([-3.5, 2.0, 7.1, 1.5, -1.0, 4.3, 9.8, 0.0, -2.2, 3.0]))    # output: 1.75
