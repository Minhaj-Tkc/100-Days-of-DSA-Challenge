class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}

        # Traverse nums2 from left to right
        for num in nums2:
            # If current num > top of stack → it is the next greater element
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)

        # Elements left in stack have no next greater element
        while stack:
            next_greater[stack.pop()] = -1

        # Prepare answer for nums1
        return [next_greater[num] for num in nums1]
