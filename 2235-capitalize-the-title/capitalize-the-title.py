class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        for i in range(len(words)):
            w = words[i]
            if len(w) <= 2:
                words[i] = w.lower()
            else:
                words[i] = w[0].upper() + w[1:].lower()
        return " ".join(words)