# 📌 Part 2 – Minimal Operations to Sort String Alphabetically

"""
1. Task:
You are given a jumbled passkey string. 
Find the minimum number of operations to arrange the string in alphabetical order.
An operation is defined by moving a single letter towards the START (to the left) of the string.
You CANNOT move letters to the right!


2. Rule:
- Crucial Rule: Since letters can ONLY move to the LEFT, any letter that has a larger letter to its left in the original string must be moved!
- Loop through the string left-to-right while keeping track of the largest letter seen so far (max_char).
- If char < max_char, it has a larger letter to its left, so it must move (moves += 1).
- If char >= max_char, it stays in place and becomes the new max_char.
"""

def min_left_shifts_to_sort(s):
    # Keep only uppercase alphabet characters
    letters = [ch for ch in s if ch.isalpha()]
    
    moves = 0
    max_so_far = ''
    
    for char in letters:
        if max_so_far == '':
            max_so_far = char
        else:
            if char < max_so_far:
                moves += 1  # This letter has a larger letter to its left, MUST move!
            else:
                max_so_far = char  # New highest letter seen so far
                
    return moves

# Example:
print(min_left_shifts_to_sort("ZXYAA")) # Ans: 4

# Input 1
print(min_left_shifts_to_sort("EVACUATIONPROTOCOLACTIVEHEHE")) # Ans: 25

# Input 2
print(min_left_shifts_to_sort("DUDESTOPMESSINGUPTHESYSTEMRICKWENEEDTOLOCKIN")) # Ans: 40

# Input 3
# Ans: 361
print(min_left_shifts_to_sort("LEAVELEAVELEAVETHISISNOTSAFELEAVEEVACUATENOWNUCLEARWARHEADLEAVELNOWNODONTIMNEVERGONNAGIVEYOUUPDONTGONONONONONONONOHELLOWORLDIMNOTTHROWINGAWAYMYSHOTOMGRICKITISTHEENDOFTHEWORLDPLEASESTOPSINGINGHAMILTONSORRYIMJUSTSTRESSSINGINGCANYOUSTOPBEINGSOMEANWARNINGWARNINGWARNINGLEAVENOWRUNEVERYONERUNTHEYARECOMINGTHISISNOTADRILLEVERYONEHIDEZXZXZXYXYZXILYCRZXPWQWXXXXXXLASTTRANSIMITTIONOFHUMANITIY")) 
