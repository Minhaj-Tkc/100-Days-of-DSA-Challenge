class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        removed = False   # to check if we already removed one number

        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:     # violation found
                if removed:
                    return False         # already removed once -> can't fix
                removed = True

                # check if removing nums[i-1] works:
                if i == 1 or nums[i] > nums[i-2]:
                    continue
                # otherwise remove nums[i], not nums[i-1]
                nums[i] = nums[i-1]

        return True
