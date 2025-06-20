class Solution:
    def generateTag(self, caption: str) -> str:
        caption = caption.strip()
        words = caption.split()

        if not words:
            return "#"
        res = "#" + words[0].lower() [:99]
        count = len(res)

        for word in words[1:]:
            newword = word.capitalize()
            if count + len(newword) > 100:
                break
            res += newword
            count += len(newword)

        return res
