class Solution:
    def isThree(self, n: int) -> bool:

        root = int(math.sqrt(n))
        # n must be a perfect square AND its square root must be a prime number
        if root * root != n:
            return False
        
        # check if root is prime
        for i in range(2, int(math.sqrt(root)) + 1):
            if root % i == 0:
                return False
        return root > 1


