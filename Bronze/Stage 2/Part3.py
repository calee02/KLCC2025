# Part 3 - Count Elements Equal to Rounded-Down Average

"""
Task: Find the floor of the average of the list. 
Count how many elements are equal to that value.

Rules to Remember / Memory Hook:
Floor Division: Use // integer division: avg_floor = sum(arr) // len(arr) (or math.floor(sum(arr) / len(arr))).
Match & Count: Count how many elements match avg_floor.
"""

def count_equal_to_floor_avg(arr):
    # Calculate rounded-down (floor) average
    avg_floor = sum(arr) // len(arr)

    count = 0

    for num in arr:
        if num == avg_floor:
            count += 1
    
    return count

"""
Input 1:
[12, 18, 24, 30, 36, 42, 48, 54, 60]
"""
print(count_equal_to_floor_avg([12, 18, 24, 30, 36, 42, 48, 54, 60])) # Ans: 1

"""
Input 2:
[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
print(count_equal_to_floor_avg([1, 2, 3, 4, 5, 6, 7, 8, 9])) # Ans: 1


"""
Input 3:
[0, 0, 0, 0, 1, 1, 1, 1]
"""
print(count_equal_to_floor_avg([0, 0, 0, 0, 1, 1, 1, 1])) # Ans: 4
