class Solution:
    def findScore(self, nums: List[int]) -> int:
        new = sorted(nums).copy()
        dic = defaultdict(deque)
        for i,n in enumerate(nums):
            dic[n].append(i)
        score = 0
        for num in new:
            idxs = dic[num]
            if idxs:
                idx = idxs.popleft()
                if nums[idx]:
                    score += nums[idx]
                    if idx>0:
                        nums[idx-1] = 0
                    if idx < len(nums)-1:
                        nums[idx+1] = 0
                    nums[idx] = 0        
        return score
        
