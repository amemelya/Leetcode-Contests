from collections import defaultdict
from collections import Counter
class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        res = 0
        picks = defaultdict(list)
        for x,y in pick:
            picks[x].append(y)
        print(picks)
        for x,y in picks.items():
            c = max(Counter(y).values())
            if c > x:
                res += 1
        return res
        
