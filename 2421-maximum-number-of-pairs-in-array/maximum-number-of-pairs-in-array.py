class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        leftovers = 0
        pairs = 0

        for num in counter.values():
            pairs += num//2
            leftovers += num%2
        
        return [pairs, leftovers]