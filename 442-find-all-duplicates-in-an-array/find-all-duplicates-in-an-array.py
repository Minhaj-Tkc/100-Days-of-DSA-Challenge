class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            index = abs(num) - 1  # Find index based on the value
            if nums[index] < 0:
                # Already visited -> duplicate found
                res.append(abs(num))
            else:
                # Mark as visited (make negative)
                nums[index] = -nums[index]

        return res