class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            # If it's a closing bracket
            if ch in mapping:
                top = stack.pop() if stack else None

                if mapping[ch] != top:
                    return False
            else:
                # It's an opening bracket
                stack.append(ch)

        return len(stack) == 0