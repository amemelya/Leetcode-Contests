class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last1 = None

        for i in range(len(nums)):
            if last1 is None and nums[i]:
                last1 = i
            elif nums[i]:
                if i - last1 <= k:
                    return False
                last1 = i
        return True
                
        
