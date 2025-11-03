class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        nums.sort(reverse=True)
        while nums:
            Alice = nums.pop()
            Bob = nums.pop()
            arr.append(Bob)
            arr.append(Alice)
        return arr