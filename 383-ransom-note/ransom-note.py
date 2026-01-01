class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = {}

        # Count characters in magazine
        for ch in magazine:
            freq[ch] = freq.get(ch, 0) + 1

        # Check ransomNote characters
        for ch in ransomNote:
            if freq.get(ch, 0) == 0:
                return False
            freq[ch] -= 1

        return True