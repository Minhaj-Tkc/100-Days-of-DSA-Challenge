class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum = 0
        num = x
        
        while num > 0:
            sum += num % 10
            num //= 10
        
        if x % sum == 0:
            return sum
        else:
            return -1 



# class Solution:
#     def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
#         digit_sum = sum(int(d) for d in str(x))
        
#         if x % digit_sum == 0:
#             return digit_sum
#         else:
#             return -1

