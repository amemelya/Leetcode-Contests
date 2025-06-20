class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        dic = defaultdict(list)
        MOD = 10**9 + 7
        res = 0
        def search(nums,target):
            l = 0
            h = len(nums) - 1
            while l<=h:
                mid = l + (h-l)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    h = mid -1
            return l
        for i,n in enumerate(nums):
            dic[n].append(i)
        for key in dic.keys():
            if key == 0:
                keyidxs = dic[key]
                for keyidx in keyidxs:
                    key2xidx = search(keyidxs,keyidx)
                    res += key2xidx * (len(keyidxs)-key2xidx-1)
                continue
            key2x = key * 2
            if dic.get(key2x,0):
                #print("key ",key, " key2x ",key2x)
                keyidxs = dic[key]
                key2xidxs = dic[key2x]
                for keyidx in keyidxs:
                    key2xidx = search(key2xidxs,keyidx)
                    #print("search ",key2xidx)
                    res += key2xidx * (len(key2xidxs)-key2xidx)
                
        return res % MOD
        
