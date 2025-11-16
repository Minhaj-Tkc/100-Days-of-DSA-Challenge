class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:

        counter = Counter(nums)

        evens = [x for x in nums if x%2 == 0]

        if not evens:
            return -1

        # find highest frequency among even numbers
        mostf = max(counter[num] for num in evens)

        evens.sort()

        for num in evens:
            if counter[num] == mostf:
                return num

        return -1