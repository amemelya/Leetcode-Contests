from collections import Counter
class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 1
        i = 0
        while i < len(word) -1:
            j = i+1
            rep = False
            while j < len(word) and word[j] == word[i]:
                rep = True
                j += 1
            if rep:
                res = res + j - i - 1
            i = j
            
        return res 
