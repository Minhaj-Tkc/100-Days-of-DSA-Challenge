class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = Counter(stones)
        count = 0

        for j in jewels:
            count += counter[j]
        
        return count