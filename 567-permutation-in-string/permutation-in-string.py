class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # Frequency arrays for a-z
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        for ch in s1:
            s1_count[ord(ch) - ord('a')] += 1
        
        l = 0
        for r in range(len(s2)):
            s2_count[ord(s2[r]) - ord('a')] += 1
            
            # Keep window size equal to len(s1)
            if r - l + 1 > len(s1):
                s2_count[ord(s2[l]) - ord('a')] -= 1
                l += 1
            
            # Compare two freq arrays
            if s1_count == s2_count:
                return True
        
        return False