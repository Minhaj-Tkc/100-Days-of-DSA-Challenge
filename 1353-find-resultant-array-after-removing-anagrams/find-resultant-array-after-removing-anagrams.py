class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        stack = []
        
        def sig(w):
            # Signature of word = sorted characters
            return "".join(sorted(w))
        
        for w in words:
            if stack and sig(stack[-1]) == sig(w):
                # They are anagrams → delete current word
                continue
            stack.append(w)
        
        return stack