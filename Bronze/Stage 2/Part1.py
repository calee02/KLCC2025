# Part 1 – Product of All Odd Numbers

"""
Task: Multiply all odd numbers in a list. If there are none, return 1.'

Rule: product * num
"""

def product_of_odds(lst):
    product = 1     # multiplication starts with 1
    has_odd = False

    for num in lst:
        if num % 2 != 0:
            product = product * num  # 1. Update product inside the loop
            has_odd = True

    # 2. Return product AFTER the loop finishes
    if has_odd:
        return product
    else: 
        return 1
            
# Input 1
"""
Input 1:
[22, 35, 5, -7, -25, -2, 31, -40, -33, -1, 36, -18, -11, 33, -47, 48, -20, -24, 41, -43]
"""
print(product_of_odds([22, 35, 5, -7, -25, -2, 31, -40, -33, -1, 36, -18, -11, 33, -47, 48, -20, -24, 41, -43])) # Ans: -942341953100625

# Input 2
"""
Input 2:
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
"""
print(product_of_odds([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])) # Ans: 1
# Input 3
"""
Input 3:
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
"""
print(product_of_odds([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])) # Ans: 654729075

