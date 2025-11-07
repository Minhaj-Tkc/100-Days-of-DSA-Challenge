class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        exptd_sum = n*(n+1)//2

        return exptd_sum - sum(nums)