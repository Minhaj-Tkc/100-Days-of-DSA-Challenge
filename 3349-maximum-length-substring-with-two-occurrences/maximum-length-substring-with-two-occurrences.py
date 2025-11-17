class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = {}
        l = 0
        max_l = 0

        for r in range(len(s)):

            count[s[r]] = count.get(s[r], 0) + 1

            while count[s[r]] > 2:
                count[s[l]] -= 1
                l += 1

            max_l = max(max_l, r-l + 1)
        
        return max_l