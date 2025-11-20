class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        # Create a list of the same size as number of words
        result = [""] * len(words)

        for w in words:
            index = int(w[-1]) - 1        # get the number at the end
            word = w[:-1]                 # remove the number from the end
            result[index] = word          # place in correct position

        return " ".join(result)

