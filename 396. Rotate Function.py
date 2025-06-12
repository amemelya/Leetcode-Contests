from collections import deque
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        s = sum(nums)
        f = 0
        for i,n in enumerate(nums):
            f += (i*n)
        res = f
        l = len(nums)
        for i in range(l-1,0,-1):
            f = f - (l*nums[i]) + s
            res = max(res,f)
        return res
            
            
        
        
       
        
