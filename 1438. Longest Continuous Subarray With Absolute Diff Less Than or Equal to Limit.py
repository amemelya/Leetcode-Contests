class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 0
        mn = min(nums[0],limit) if abs(limit - nums[0]) <= limit else nums[0]
        mx = max((nums[0],limit)) if abs(limit - nums[0]) <= limit else nums[0]
        count = 1 if abs(limit - nums[0]) <= limit else 0
        res = max(res,count)
        s = 0
        for i in range(1,len(nums)):
            mn = min(mn,nums[i])
            mx = max(mx,nums[i])
            print("mn", mn)
            print("mx",mx)
            if mx - mn <= limit:
                count += 1
                print(nums[s:i+1])
                print("count ",count)
            else :
                mi = mn
                ma = mxcan 
                #abs(nums[i]-nums[s])
                while i < len(nums) and abs(ma-mi) > limit:
                    s += 1
                count = max(i-s+1,1)
                print("count new",count)
                if i == s:
                    mn = min(nums[s],limit) if abs(limit - nums[s]) <= limit else nums[s]
                    mx = max(nums[s],limit) if abs(limit - nums[s]) <= limit else nums[s]
                else:
                    mn = min(nums[i],nums[s])
                    mx = max(nums[i],nums[s])
            res = max(res,count)
            
        return res
                
            
            
        
