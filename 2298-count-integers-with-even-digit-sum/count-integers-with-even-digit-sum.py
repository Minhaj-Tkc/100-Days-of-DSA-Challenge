class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        
        for i in range(1, num + 1):
            digit_sum = sum(int(d) for d in str(i))
            if digit_sum % 2 == 0:
                count += 1
        
        return count


# class Solution:
#     def countEven(self, num: int) -> int:
#         s = sum(int(d) for d in str(num))
#         return (num - 1) // 2 if s % 2 else num // 2
