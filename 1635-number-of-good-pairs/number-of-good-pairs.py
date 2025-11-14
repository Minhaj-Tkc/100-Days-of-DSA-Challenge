class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = Counter(nums)
        count = 0
        
        for k in freq.values():
            count += k * (k - 1) // 2
        
        return count
                   