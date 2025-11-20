class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {}
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        idx = 0

        # Build mapping from key → alphabet
        for ch in key:
            if ch != ' ' and ch not in mapping:
                mapping[ch] = alphabet[idx]
                idx += 1

        # Decode the message
        result = []
        for ch in message:
            if ch == ' ':
                result.append(' ')
            else:
                result.append(mapping[ch])

        return "".join(result)