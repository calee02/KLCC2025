# Part 6 – Sum of All Digits

"""
Task: Compute the sum of all digits of all numbers in a list.

Rule: outer loop for numbers, inner loop for digit
"""

def sum_of_all_digits(lst):
    sum = 0
    for num in lst:
        for char in str(abs(num)):  # Turn number into a string of digits
            sum += int(char)      # Turn digit back to number and add
    return sum

# Example
"""
Input: [12, 34]
Output: 10
"""
print(sum_of_all_digits([12, 34])) # Ans: 10

# Input 1
"""
Input 1: [12, 45, 67, 89, 23, 56, 90, 34, 78, 10]
"""
print(sum_of_all_digits([12, 45, 67, 89, 23, 56, 90, 34, 78, 10])) # Ans: 90

# Input 2
"""
Input 2: [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
"""
print(sum_of_all_digits([11, 22, 33, 44, 55, 66, 77, 88, 99, 100])) # Ans: 91
 