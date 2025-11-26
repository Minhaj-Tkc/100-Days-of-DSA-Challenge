class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:        
        collected = set()
        operations = 0
        
        for num in reversed(nums):
            operations += 1
            if 1 <= num <= k:
                collected.add(num)
            if len(collected) == k:
                break
        
        return operations