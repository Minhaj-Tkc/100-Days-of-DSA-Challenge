class Solution:
    def isFascinating(self, n: int) -> bool:
        # Step 1: concatenate n, 2n, 3n
        s = str(n) + str(2*n) + str(3*n)

        # Step 2: check conditions
        # Must be exactly 9 digits
        if len(s) != 9:
            return False
        
        # Should contain digits 1–9 exactly once
        return set(s) == set("123456789")
