class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # If they cannot form each other by repetition, no common divisor exists
        if str1 + str2 != str2 + str1:
            return ""
        
        # Otherwise, answer is the prefix of length gcd(len1, len2)
        from math import gcd
        length = gcd(len(str1), len(str2))
        return str1[:length]