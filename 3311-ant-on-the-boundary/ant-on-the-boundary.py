class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        position = 0   # ant starts at the boundary
        count = 0      # how many times it returns to boundary
        
        for move in nums:
            position += move  # move left or right
            if position == 0:
                count += 1    # ant returned to boundary
        
        return count