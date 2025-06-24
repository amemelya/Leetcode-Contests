
from collections import Counter
class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def isprime(num):
            if num <= 1:
                return False
            if num == 2:
                return True
            for n in range(2,(num//2)+1):
                if num % n == 0:
                    return False
            return True
        counts = Counter(nums)
        #print(counts)
        for k,v in counts.items():
            if isprime(v):
                #print(k)
                return True
        return False
        
