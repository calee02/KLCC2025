# 📌 Part 1 - Highest Uninterrupted Sum & Permutations of Positions

"""
Task: 
- finding which elements will yield the highest uninterrupted sum 
- given a sequence of integers containing -1 values, where -1 acts as a reset button for the continuous sum
- Print all lexicographical permutations of those position numbers in a single line

Rule: 
- Segment & Reset: Keep adding numbers to a current_sum. 
  Whenever you hit -1, compare current_sum with max_sum, save the winning positions, and reset current_sum = 0
- Permutations Magic: Use Python's itertools.permutations() to automatically shuffle the winning position numbers in alphabetical/numeric order

Simpler explanations:
* Positive numbers give you points!
* -1 is a BOMB! Hitting a bomb resets your current score streak back to 0.
* Your Job:
    + Find the streak between bombs that gave the highest score.
    + Take the box numbers (1st box, 2nd box, 3rd box, etc.) of that winning streak.
    + Print all possible arrangements (permutations) of those box numbers in order!

** Note: lexicographically - alphabetically order
"""

import itertools

def hack_omega_firewall(boxes):
    highest_score = -1
    winning_boxes = []

    current_score = 0
    current_boxes = []

    # 1. loop through the boxes (box position starts at 1)
    for pos, val in enumerate(boxes, start=1):
        if val == -1:
            # Hit a bomb! Check if this streak was our best yet
            if current_score > highest_score:
                highest_score = current_score
                winning_boxes = current_boxes
            
            # Reset streak
            current_score = 0 
            current_boxes = []
        else: 
            current_score += val
            current_boxes.append(pos)

    # Check the final streak after the loop
    if current_score > highest_score:
        highest_score = current_score
        winning_boxes = current_boxes
    
    # 2. Find all shuffles (permutations) of the winning box positions
    all_shuffles = sorted(list(itertools.permutations(winning_boxes)))

    # 3. Format as a single line
    result_words = []
    for shuffle in all_shuffles:
        result_words.append(" ".join(map(str, shuffle)))

    return " ".join(result_words)

def parse_arr(raw_arr):
    cleaned = raw_arr.replace("[","").replace("]","").strip()

    if not cleaned:
        return []
    
    return [int(x) for x in cleaned.split()]


# Example
"""
Input:
1 2 3 -1 3 50 5 -1 2
Output:
5 6 7 5 7 6 6 5 7 6 7 5 7 5 6 7 6 5
"""
raw_arr = input("Enter the input: ")
print("=" * 55)
print(hack_omega_firewall(parse_arr(raw_arr)))
# Ans: 5 6 7 5 7 6 6 5 7 6 7 5 7 5 6 7 6 5


# Input 1
# Ans: 1 2 3 4 5 1 2 3 5 4 1 2 4 3 5 1 2 4 5 3 1 2 5 3 4 1 2 5 4 3 1 3 2 4 5 1 3 2 5 4 1 3 4 2 5 1 3 4 5 2 1 3 5 2 4 1 3 5 4 2 1 4 2 3 5 1 4 2 5 3 1 4 3 2 5 1 4 3 5 2 1 4 5 2 3 1 4 5 3 2 1 5 2 3 4 1 5 2 4 3 1 5 3 2 4 1 5 3 4 2 1 5 4 2 3 1 5 4 3 2 2 1 3 4 5 2 1 3 5 4 2 1 4 3 5 2 1 4 5 3 2 1 5 3 4 2 1 5 4 3 2 3 1 4 5 2 3 1 5 4 2 3 4 1 5 2 3 4 5 1 2 3 5 1 4 2 3 5 4 1 2 4 1 3 5 2 4 1 5 3 2 4 3 1 5 2 4 3 5 1 2 4 5 1 3 2 4 5 3 1 2 5 1 3 4 2 5 1 4 3 2 5 3 1 4 2 5 3 4 1 2 5 4 1 3 2 5 4 3 1 3 1 2 4 5 3 1 2 5 4 3 1 4 2 5 3 1 4 5 2 3 1 5 2 4 3 1 5 4 2 3 2 1 4 5 3 2 1 5 4 3 2 4 1 5 3 2 4 5 1 3 2 5 1 4 3 2 5 4 1 3 4 1 2 5 3 4 1 5 2 3 4 2 1 5 3 4 2 5 1 3 4 5 1 2 3 4 5 2 1 3 5 1 2 4 3 5 1 4 2 3 5 2 1 4 3 5 2 4 1 3 5 4 1 2 3 5 4 2 1 4 1 2 3 5 4 1 2 5 3 4 1 3 2 5 4 1 3 5 2 4 1 5 2 3 4 1 5 3 2 4 2 1 3 5 4 2 1 5 3 4 2 3 1 5 4 2 3 5 1 4 2 5 1 3 4 2 5 3 1 4 3 1 2 5 4 3 1 5 2 4 3 2 1 5 4 3 2 5 1 4 3 5 1 2 4 3 5 2 1 4 5 1 2 3 4 5 1 3 2 4 5 2 1 3 4 5 2 3 1 4 5 3 1 2 4 5 3 2 1 5 1 2 3 4 5 1 2 4 3 5 1 3 2 4 5 1 3 4 2 5 1 4 2 3 5 1 4 3 2 5 2 1 3 4 5 2 1 4 3 5 2 3 1 4 5 2 3 4 1 5 2 4 1 3 5 2 4 3 1 5 3 1 2 4 5 3 1 4 2 5 3 2 1 4 5 3 2 4 1 5 3 4 1 2 5 3 4 2 1 5 4 1 2 3 5 4 1 3 2 5 4 2 1 3 5 4 2 3 1 5 4 3 1 2 5 4 3 2 1

# Input 2
# Ans: 157 158 159 160 157 158 160 159 157 159 158 160 157 159 160 158 157 160 158 159 157 160 159 158 158 157 159 160 158 157 160 159 158 159 157 160 158 159 160 157 158 160 157 159 158 160 159 157 159 157 158 160 159 157 160 158 159 158 157 160 159 158 160 157 159 160 157 158 159 160 158 157 160 157 158 159 160 157 159 158 160 158 157 159 160 158 159 157 160 159 157 158 160 159 158 157

# Input 3
# Ans: 129