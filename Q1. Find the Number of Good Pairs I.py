class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] % (nums2[j] * k) == 0:
                    res += 1
        return res


        ©leetcode
