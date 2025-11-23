class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []

        for word in words:
            parts = word.split(separator)
            for p in parts:
                if p != "":            # ignore empty strings
                    result.append(p)
                    
        return result