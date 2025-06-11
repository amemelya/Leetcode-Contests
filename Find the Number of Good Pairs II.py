from collections import Counter

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        maxval = max(nums1)
        n1freq = Counter(nums1)
        res = 0
        n2freq = Counter(nums2)
        for num in set(nums2):
            multiple = num * k
            while multiple <= maxval:
                res += n1freq.get(multiple, 0) * n2freq.get(num,0)
                multiple += num * k
                
        return res
©leetcode
