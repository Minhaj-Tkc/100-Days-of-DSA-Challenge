class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0  
                     
        for i in range(1, n + 1):
            if i % m == 0:
                num2 += i
            else:
                num1 += i
    
        return num1 - num2

# class Solution:
#     def differenceOfSums(self, n: int, m: int) -> int:
#         total_sum = n * (n + 1) // 2  # sum of 1..n
#         k = n // m                    # count of multiples of m
#         div_sum = m * k * (k + 1) // 2  # sum of multiples of m
#         return total_sum - 2 * div_sum
