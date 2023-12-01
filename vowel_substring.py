"""
Finds the substring of length k in the given string s
that contains the maximum number of vowels. 
If multiple substrings have the same max_vowels, 
it chooses the one with the lowest index.

Args:
    s (str): The input string.
    k (int): The length of the substring.

Returns:
    str: The substring with the maximum number of vowels,
            or 'Not found!' if no vowels are present.
"""

def findSubstring(s, k):
    max_vowels = 0
    max_vowel_substr = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    found_vowel = False

    current_substring = s[:k]
    current_vowels = sum(1 for char in current_substring if char in vowels)

    for i in range(len(s) - k + 1):
        if s[i - 1] in vowels:
            current_vowels -= 1
        if s[i + k - 1] in vowels:
            current_vowels += 1
        if current_vowels > max_vowels:
            max_vowels = current_vowels
            max_vowel_substr = s[i:i+k]
            found_vowel = True
        elif current_vowels == max_vowels and i < s.index(max_vowel_substr):
            max_vowel_substr = s[i:i+k]

        if max_vowels == k:
            return max_vowel_substr

    if not found_vowel:
        return 'Not found!'

    return max_vowel_substr


result = findSubstring('eiuaooo', 4)

if result != 'Not found!':
    print(f"The substring with the maximum number of vowels is: {result}")
else:
    print("No vowels found in the substring.")