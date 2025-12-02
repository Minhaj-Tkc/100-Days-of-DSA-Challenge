class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = 1

        for n in nums:
            if n == 0:
                return 0      # product becomes zero immediately
            if n < 0:
                sign = -sign  # flip sign
        
        return sign