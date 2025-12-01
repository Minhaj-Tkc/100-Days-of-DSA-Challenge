class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        n = len(s)

        start = 0

        for end in range(n + 1):
            if end == n or s[end] == " ":
                # reverse the word between start and end-1
                left, right = start, end - 1
                while left < right:
                    s[left], s[right] = s[right], s[left]
                    left += 1
                    right -= 1
                start = end + 1  # move to next word
        return "".join(s)