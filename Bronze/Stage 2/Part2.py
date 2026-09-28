# Part 2 - Count Local Peaks (Greater Than Neighbors)

"""
Task: Count how many elements are larger than both neighbours. First/last elements don't count.

Rules:
Range Skip: Loop from index 1 up to len(arr) - 2 so you don't check beyond list boundaries.
Peak Condition: arr[i] > arr[i - 1] and arr[i] > arr[i + 1]
"""

def count_peaks(arr):
    count = 0

    # start at index 1, stop before last element
    for i in range(1, len(arr)-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            count +=1
    return count 

"""
Input 1:
[1, 3, 2, 4, 5, 1, 7, 0, 8, 2, 6, 1, 9]
"""
print(count_peaks([1, 3, 2, 4, 5, 1, 7, 0, 8, 2, 6, 1, 9])) # Ans: 5


"""
Input 2:
[5, 5, 5, 5, 5, 5, 5, 5, 5]
"""
print(count_peaks([5, 5, 5, 5, 5, 5, 5, 5, 5])) # ans: 0


"""
Input 3:
[10, 20, 15, 30, 25, 35, 30, 40, 20]
"""
print(count_peaks([10, 20, 15, 30, 25, 35, 30, 40, 20])) # Ans: 4
