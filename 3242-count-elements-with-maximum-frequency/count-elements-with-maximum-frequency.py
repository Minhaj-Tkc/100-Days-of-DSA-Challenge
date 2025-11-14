class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_freq = max(freq.values())
        
        total = 0
        for f in freq.values():
            if f == max_freq:
                total += f
        
        return total