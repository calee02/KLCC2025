# Part 1 - Count of Numbers Greater Than 5

"""
Task: Output the count of numbers in a list that are greater than 5.

Rule: x > 5
"""

def count_greater_than_5(lst):
    count = 0
    for x in lst:
        if x > 5:
            count += 1
    return count

# Example 
print(count_greater_than_5([3, 6, 8, 2, 5])) # Ans: 2

# Input 1
print(count_greater_than_5([7, 2, 10, 4, 5, 6, 1, 8, 3, 9, 11])) # Ans: 6

# Input 2 
print(count_greater_than_5([1, 4, 5, 6, 7, 0, 2, 8, 3, 9, 8])) # Ans: 5
