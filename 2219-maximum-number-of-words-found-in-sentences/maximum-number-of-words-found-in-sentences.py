class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0

        for sentence in sentences:
            words = len(sentence.split())
            if max_words < words:
                max_words = words
        
        return max_words
