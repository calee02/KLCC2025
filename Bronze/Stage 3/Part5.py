# 📌 Part 5 – Geometric Initial Supply ($a$)

"""
Task: Using the formula G_n = a(1 - r)^{n - 1}
find the initial supply a rounded to the nearest integer given G_n, r, and n.

Rule: Divide G_n by (1 - r)^{n - 1}, 
then use round() to get the nearest whole number.
"""

def find_initial_supply(Gn, r, n):
    a = Gn / ( (1-r) ** (n-1) )
    return round(a)

# Example:
"""
Input: G4 = 343, r = 0.3
Output: 1000
"""
print(find_initial_supply(343, 0.3, 4)) # Ans: 1000

# Input
"""
Input: G997 = 431189095, r = 0.0006
"""
print(find_initial_supply(431189095, 0.0006, 997)) # Ans: 783934978
