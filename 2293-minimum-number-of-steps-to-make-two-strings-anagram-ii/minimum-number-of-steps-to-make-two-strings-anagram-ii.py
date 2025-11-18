class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)

        count = 0

        for ch in set(count_s.keys()).union(count_t.keys()):
            count += abs(count_s[ch] - count_t[ch])
        
        return count

        