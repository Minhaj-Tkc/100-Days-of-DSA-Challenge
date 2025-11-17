class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        set_nums = set(nums)
        count  = 0

        for num in nums:
            if num + diff in set_nums and num + 2*diff in set_nums:
                count += 1
        
        return count
