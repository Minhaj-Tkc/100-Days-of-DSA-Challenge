class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        
        divisor_sum = 1  # 1 is always a divisor
        
        # Only check up to sqrt(num)
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                divisor_sum += i
                if i != num // i:  # Avoid adding square root twice
                    divisor_sum += num // i
        
        return divisor_sum == num