class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        finalNums = []
        finalNums.append([1])  # first row

        for i in range(numRows - 1):  # we already have row 1
            newRow = [1]              # every row starts with 1

            # fill middle values
            for j in range(i):
                newRow.append(finalNums[i][j] + finalNums[i][j+1])

            newRow.append(1)          # every row ends with 1
            finalNums.append(newRow)

        return finalNums