class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        for i in range(len(flowerbed)):
            # check current plot
            if flowerbed[i] == 0:
                # check left
                if i > 0 and flowerbed[i - 1] == 1:
                    continue

                # check right
                if i < len(flowerbed) - 1 and flowerbed[i + 1] == 1:
                    continue

                # plant flower
                flowerbed[i] = 1
                n -= 1

                if n == 0:
                    return True

        return False