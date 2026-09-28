# 📌 Part 10 – Palindromic Circuit Code

"""
Task: 
- Clean the string (lowercase, remove spaces). 
- If it's not a palindrome, return -1. 
- If it is a palindrome, return the first half string S (where S + S_{reversed} = \text{cleaned code}).

** palindrome (reads the same forwards and backwards)

Rule:
1. Clean text: convert to lowercase and remove spaces.
2. Check if text == text[::-1]. If not, return -1.
3. If it matches, return the first half: text[:len(text)//2].
"""

def check_circuit_code(code):
    # clean text: lowercase and remove spaces
    cleaned = code.lower().replace(" ", "")

    # check if palindrome
    if cleaned != cleaned[::-1]:
        return -1
    
    # return first half 
    half_len = len(cleaned) // 2
    return cleaned[:half_len]

# Example 1
"""
Input: “Race car”
Output: “race”
Explanation: After removing spaces and converting to lowercase, it becomes “racecar”, which is a
palindrome. When “race” is concatenated with “ecar”, it becomes “racecar”, so the string S is “race”.
Note: the concatenation does not result in the string “raceecar” in this case.
"""
print(check_circuit_code("Race car"))

# Example 2
"""
Input: “nOon”
Output: “no”
Explanation: After converting to lowercase, it becomes “noon”, which is a palindrome. When “no” is
concatenated with “on”, it becomes “noon”, so the string S is “no”.
"""
print(check_circuit_code("nOon"))

# Input
print(check_circuit_code("able was I ere I saw elba a man a plan a canal panama no lemon no melon a santa at nasaMadam in Eden I'm Adam step on no pets racecar never odd or even evil is a name of a foeman as Ilive aibohphobia a man a plan a canal panama a dolphin lived and evil is a name of a foeman as I liveno lemon no melon a cat a fat cat a man a plan a canal panama no lemon no melon racecar a Santaat NASA I saw Bob no lemon no melon a man a plan a canal panama able was I ere I saw elba a mana plan a canal panama no lemon no melon a santa at nasa Madam in Eden I'm Adam step on no petsracecar never odd or even evil is a name of a foeman as I live aibohphobia a man a plan a canalpanama a dolphin lived and evil is a name of a foeman as I live no lemon no melon a cat a fat cat aman a plan a canal panama no lemon no melon racecar a Santa at NASA I saw Bob no lemon nomelon a man a plan a canal panama able was I ere I saw elba"))
# Ans: -1