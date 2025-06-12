from collections import defaultdict
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.dic = defaultdict(list)
        for i in range(len(self.nums)):
            self.dic[self.nums[i]].append(i)
    def pick(self, target: int) -> int:
        indxs = self.dic[target]
        return indxs[random.randrange(0,len(indxs))]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
