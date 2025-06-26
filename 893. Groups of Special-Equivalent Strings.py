class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        visited= set()
        groups = len(words)
        for i in range(len(words)):
            odddic = Counter(words[i][0::2])
            evendic = Counter(words[i][1::2])
            for j in range(i+1,len(words)):
                if j in visited:
                    continue
                odic = Counter(words[j][0::2])
                edic = Counter(words[j][1::2])
                if odddic == odic and evendic == edic:
                    visited.add(i)
                    visited.add(j)
                    groups -= 1
                
        return groups
            
        
