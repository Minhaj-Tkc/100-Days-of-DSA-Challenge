class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        drops = 0
        drop_index = -1
        
        for i in range(n - 1):
            if nums[i] > nums[i+1]:
                drops += 1
                drop_index = i
        
        # Check the circular edge
        if nums[-1] > nums[0]:
            drops += 1
            drop_index = n - 1
        
        # If more than one drop → impossible
        if drops > 1:
            return -1
        
        # Already sorted
        if drops == 0:
            return 0
        
        # Otherwise shifts required:
        return n - (drop_index + 1)