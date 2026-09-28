# 📌 Part 1 – Most Frequent Letter Dominance Ratio

"""
Task: You’re calculating how “dominant” the most common letter is in a transmission.
1. Count total letters (A–Z, ignoring case)
2. Find how often the most frequent one appears
3. Divide (most frequent/total letters)

Rule:
1. Clean the text: keep only letters a-z (char.isalpha()) and convert them to lowercase
2. Count total letters (len(letters)).
3. Use collections.Counter to find the highest letter frequency
4. Return round(max_count / total_letters, 4)
"""

import collections

def letter_dominance_ratio(text):
    letters = [ch.lower() for ch in text if ch.isalpha()]

    if not letters:
        return 0.0
    
    # Count letter frequencies
    counts = collections.Counter(letters)
    max_count = max(counts.values())

    # Calculate ratio rounded to 4 decimals
    return round(max_count / len(letters), 4)

# Example
# Ans: 0.1449
print(letter_dominance_ratio("T-minus five minutes until detonation sequence activation. Evacuate immediately!"))

# Input 1
# Ans: 0.1288
print(letter_dominance_ratio("Yall im so scared lol what if they actually throw the bomb are we gonna die or something. Omg Rick shush you are messing with the audio please we need to decode this."))

# Input 2
# Ans: 0.0741
print(letter_dominance_ratio("Jnkbhuvgtycrtxewzwzsxedrcftvgybhunijmok,mijuhygtrfedddrcvbuhnimowcijnruvhebgyhelphelphelphelphelpmjnihbugvyfctdxrctryuinjonibuvyctfvgbhnmjjuhygtyg67unjmuhygvttfcdxrsdcfgvhbjnihygtvbvetrbrwejnbdsvtuybeijgoikweoivuherbnjgekfwiocdsvufhbhejnkgrwfepciojvuhbgnjrkwmefkojivuhbrgnjwefoqmajciuhvywgrhbgwejifuvhrg\sdcnjwefnonononononononoanoubefiyvwubhijnofqiuiwybvhjanifoquhwgirvhbjnsdkmaioeuibwjklrbknvfsdiouhiafgyewbhkjrgnboufhiygutfyrdexrdtcfyvgubhinjytgfgbhkjnkiuhvfej-vwkwuhgeihavonljwbeuhwioeglkvjnkij8978hygqebhijfwrbuiwgy23qenjmvribeojtuhetnjmlkweigjoriuhbnjfslvmkpeqiughirtbnjgmkoiybutvycrfvghjiygtfrdectfgvhbjmuih/csygfrvghjoklmsvfbeiwreiokrmvflbgerynthrgbergehrytjukyjmnh"))

# Input 3
print(letter_dominance_ratio(""))
