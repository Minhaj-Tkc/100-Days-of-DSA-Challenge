class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter_s = Counter(s)
        counter_t = Counter(t)

        count = 0
        for ch in counter_s:
            if counter_s[ch] > counter_t.get(ch, 0):
                count += counter_s[ch] - counter_t.get(ch, 0)
        
        return count