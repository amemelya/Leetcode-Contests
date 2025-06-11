class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        i = 0
        prev = word[0]
        count = 0
        while i < len(word):
            if prev == word[i]:
                if count == 9:
                    comp = comp + str(count) + prev
                    count = 0
                count += 1
            else:
                comp = comp + str(count) + prev
                prev = word[i]
                count = 1
            i+= 1
        comp = comp + str(count) + prev
        return comp



        ©leetcode
