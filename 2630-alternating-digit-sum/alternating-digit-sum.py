class Solution:
    def alternateDigitSum(self, n: int) -> int:
        sumdigit = 0
        for i, d in enumerate(str(n)):
            if i % 2 == 0:      #( "%" ~20–40 CPU Cycles - involves a division inside )
                sumdigit += int(d)
            else:
                sumdigit -= int(d)
        
        return sumdigit

# ⭐ Fastest and cleanest 
# class Solution:
#     def alternateDigitSum(self, n: int) -> int:
#         s = str(n)
#         total = 0
#         sign = 1
#         for ch in s:
#             total += sign * int(ch)
#             sign *= -1   # ( "*" ~3 CPU Cycles )
#         return total

            