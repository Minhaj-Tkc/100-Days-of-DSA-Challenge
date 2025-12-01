class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        stack = []

        for char in s:
            if char != " ":
                stack.append(char)
            else:
                while stack:
                    result.append(stack.pop())
                result.append(" ")
        while stack:
            result.append(stack.pop())

        return "".join(result)