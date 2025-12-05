class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        #from itertools import zip_longest
        
        res = []

        for a, b in zip_longest(word1, word2, fillvalue=""):
            res.append(a)
            res.append(b)

        return "".join(res)