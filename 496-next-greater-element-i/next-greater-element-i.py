class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for x in nums1:
            # find index of x in nums2
            index = nums2.index(x)

            # look to the right for the next greater element
            next_greater = -1
            for j in range(index + 1, len(nums2)):
                if nums2[j] > x:
                    next_greater = nums2[j]
                    break

            ans.append(next_greater)

        return ans
