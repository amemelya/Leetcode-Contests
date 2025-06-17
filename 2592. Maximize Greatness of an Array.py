class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        l = 0
        r = 1
        res = 0
        nums.sort()
    
        while r < len(nums):
            while r < len(nums) and nums[r] <= nums[l]:
                r += 1
            if r < len(nums):
                res += 1
            l += 1
            r += 1
        return res
            
        
