class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        L = moves.count("L") 
        R = moves.count("R") 
        _ = moves.count("_") 
            
        if L < R:
            return (R + _) - L
        else:
            return (L + _) - R
