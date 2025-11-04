class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        total_sum = 0
        
        while n>0:
            d = n%10
            product *= d
            total_sum += d
            n = n//10
        
        return product - total_sum

# class Solution:
#     def subtractProductAndSum(self, n: int) -> int:
#         product = 1
#         total_sum = 0
        
#         for digit in str(n):
#             d = int(digit)
#             product *= d
#             total_sum += d
        
#         return product - total_sum