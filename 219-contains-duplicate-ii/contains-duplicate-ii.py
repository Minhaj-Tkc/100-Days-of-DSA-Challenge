class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for i, num in enumerate(nums):

            # If number already in window → duplicate found
            if num in window:
                return True

            # Add current number to window
            window.add(num)

            # Maintain window size <= k
            if len(window) > k:
                window.remove(nums[i - k])

        return False
