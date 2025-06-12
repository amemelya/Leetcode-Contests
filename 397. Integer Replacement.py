class Solution:
    def integerReplacement(self, n: int) -> int:
        res = 0

        while n > 1:
            if n % 2 == 0:
                n = n//2
            elif (n-1)//2 % 2 == 0 or n-1 == 2:
                n = n - 1
            else:
                n = n + 1
            res += 1
        return res
                
        
