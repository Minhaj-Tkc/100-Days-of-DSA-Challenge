class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        zeros = arr.count(0)   # Count how many zeros we need to duplicate
        i = n - 1
        j = n + zeros - 1      # Virtual end index after duplicating

        while i < j:
            if arr[i] != 0:
                if j < n:
                    arr[j] = arr[i]
            else:
                if j < n:
                    arr[j] = 0
                j -= 1
                if j < n:
                    arr[j] = 0
            i -= 1
            j -= 1


