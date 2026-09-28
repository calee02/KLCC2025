# Part 5: Number of Even Integers

"""
Task: Count how many numbers in a list are even.

Rule: num % 2 == 0 (Remainder when divided by 2 is zero)
"""

def count_evens(lst):
    count = 0
    for x in lst:
        if x % 2 == 0:
            count+=1
    return count

# Example
"""
Example:
Input: [1, 2, 3, 4]
Output: 2
"""
print(count_evens([1, 2, 3, 4])) # Ans: 2

# Input 1
"""
Input 1: [2, 4, 6, 8, 10, 11, 13, 15, 17, 20]
"""
print(count_evens([2, 4, 6, 8, 10, 11, 13, 15, 17, 20])) # Ans: 6


# Input 2
"""
Input 2: [1, 3, 5, 7, 9, 12, 14, 16, 18, 19]
"""
print(count_evens([1, 3, 5, 7, 9, 12, 14, 16, 18, 19])) # Ans: 4