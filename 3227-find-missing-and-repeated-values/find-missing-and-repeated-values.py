class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        n = len(grid)
        arr = [num for col in grid for num in col]
        freq = Counter(arr)
        
        a = b = -1
        for i in range(1, n*n + 1):
            if freq[i] == 2:
                a = i
            elif freq[i] == 0:
                b = i
        
        return [a, b]



        