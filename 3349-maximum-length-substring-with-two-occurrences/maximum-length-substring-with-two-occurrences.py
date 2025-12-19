class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        counter = defaultdict(int)
        l = 0
        max_l = 0

        for r in range(len(s)):
            counter[s[r]] += 1
            
            while 2<counter[s[r]]:
                counter[s[l]] -= 1
                l += 1
            
            max_l = max(max_l, r-l+1)
        
        return max_l
