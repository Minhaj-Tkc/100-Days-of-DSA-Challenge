class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        start, end = s.split(":")
        
        col1, row1 = start[0], int(start[1:])
        col2, row2 = end[0], int(end[1:])
        
        result = []
        
        for c in range(ord(col1), ord(col2) + 1):
            for r in range(row1, row2 + 1):
                result.append(chr(c) + str(r))
        
        return result