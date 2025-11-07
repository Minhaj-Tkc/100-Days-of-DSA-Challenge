class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels =  {'a', 'e', 'i', 'o', 'u'}

        maxv = 0
        maxc = 0
        for w in set(s):
            if w in vowels:
                maxv = max(s.count(w), maxv)
            else:
                maxc = max(s.count(w), maxc)

        return maxv + maxc



# class Solution:
#     def maxVowelConsonantSum(self, s: str) -> int:
#         vowels = set('aeiou')
#         vowel_count = {}
#         consonant_count = {}
        
#         # Count frequency of vowels and consonants
#         for ch in s:
#             if ch in vowels:
#                 vowel_count[ch] = vowel_count.get(ch, 0) + 1
#             else:
#                 consonant_count[ch] = consonant_count.get(ch, 0) + 1
        
#         # Find max frequency among vowels and consonants
#         max_vowel = max(vowel_count.values()) if vowel_count else 0
#         max_consonant = max(consonant_count.values()) if consonant_count else 0
        
#         return max_vowel + max_consonant

