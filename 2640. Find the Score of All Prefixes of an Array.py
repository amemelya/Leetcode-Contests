class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        res = []
        score = 0
        m = 0
        for num in nums:
            if num > m:
                score = score + num + num
                m = num
            else:
                score = score + num + m
            res.append(score)
        return res
        
