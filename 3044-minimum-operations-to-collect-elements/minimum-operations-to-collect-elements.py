class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:        
        need = set(range(1, k+1))
        n = len(nums)

        for i in range(n-1, -1, -1):
            if nums[i] in need:
                need.remove(nums[i])
            if not need:  # all collected
                return n - i