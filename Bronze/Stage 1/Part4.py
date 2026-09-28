# Part 4 – Coordinates on Line

"""
Task: Count how many coordinates (x, y) satisfy the given line equation.

Rule: y == m * x + c
"""

def coordinates_on_line(coords, m, c):
    count = 0
    for x, y in coords:
        if y == m * x + c:
            count += 1
    return count

# Example 
"""
Equation: y = 2x + 1
Input: [[0, 1], [1, 3], [2, 4]]
Output: 2
"""
me, ce = 2, 1
print(coordinates_on_line([[0, 1], [1, 3], [2, 4]], me, ce)) # Ans: 2

# Input 1
"""
Input 1: Equation y = 2x + 3
Coordinates: [[0, 3], [1, 5], [2, 7], [3, 9], [4, 11], [5, 13], [1, 6], [2, 5], [6, 15], [7, 17]]
"""
m1, c1 = 2, 3
coor1 = [[0, 3], [1, 5], [2, 7], [3, 9], [4, 11], [5, 13], [1, 6], [2, 5], [6, 15], [7, 17]]
print(coordinates_on_line(coor1, m1, c1)) # Ans: 8

# Input 2
"""
Input 2: Equation y = −x + 4
Coordinates: [[0, 4], [1, 3], [2, 2], [3, 1], [4, 0], [5, −1], [6, −2], [3, 2], [2, 3], [−1, 5]]
"""
m2, c2 = -1, 4
coor2 = [[0, 4], [1, 3], [2, 2], [3, 1], [4, 0], [5, -1], [6, -2], [3, 2], [2, 3], [-1, 5]]
print(coordinates_on_line(coor2, m2, c2)) # Ans: 8
