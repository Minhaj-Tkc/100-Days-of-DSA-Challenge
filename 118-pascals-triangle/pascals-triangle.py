class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for r in range(numRows):
            # start each row with 1s
            row = [1] * (r + 1)

            # fill inner values (if any)
            for c in range(1, r):
                row[c] = res[r-1][c-1] + res[r-1][c]

            res.append(row)

        return res