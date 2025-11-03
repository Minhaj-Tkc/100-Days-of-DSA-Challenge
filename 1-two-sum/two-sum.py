class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # key = number, value = index

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]  # found

            seen[num] = i  # store number with its index

