class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        res = []
        m = min(len(word1), len(word2))

        for i in range(m):
            res.append(word1[i])
            res.append(word2[i])

        res.append(word1[m:])
        res.append(word2[m:])

        return "".join(res)