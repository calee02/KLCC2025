# 📌 Part 4 – Linear Depletion Rate (d)

"""
Task: Using the formula A_n = a + (n - 1)d, find the daily depletion rate (d) given A_n, a, and n.

Rule: 
Rearrange the algebra formula: subtract initial supply a from A_n, then divide by (n - 1).
"""

def find_depletion_rate(An, a, n):
    return (An - a) // (n-1)

# Example:
"""
Input: A4 = 5, a = 14
Output: d = -3
Explanation: A4 = 14 + (4 - 1) x -3 = 14 + 3 x -3 = 14 - 9 = 5.
"""
print(find_depletion_rate(5, 14, 4))

# Input 1
"""
Input: A997 = 7023824990, a = 173957246803
"""
print(find_depletion_rate(7023824990, 173957246803, 997)) # Ans: -167603838