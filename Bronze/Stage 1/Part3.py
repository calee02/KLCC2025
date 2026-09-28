# Part 3 - Multiples of 11

"""
Task: Count the numbers in a list that are multiples of 11.

Rule: x % 11 == 0 (Remainder when divided by 11 is zero)
"""

def multiples_of_11(lst):
    count = 0
    for x in lst:
        if x % 11 == 0:
            count+=1
    return count

# Example
print(multiples_of_11([11, 22, 5, 33])) # Ans: 3

# Input 1
print(multiples_of_11([11, 22, 33, 44, 55, 60, 70, 77, 80, 99])) # Ans: 7

# Input 2
print(multiples_of_11([5, 10, 15, 22, 30, 33, 44, 50, 60, 121])) # Ans: 4