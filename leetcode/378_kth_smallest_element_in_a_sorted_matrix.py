class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        low = matrix[0][0]
        high = matrix[n - 1][n - 1]
        def countLessEqual(x):
            i = n - 1
            j = 0
            count = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= x:
                    count += i + 1
                    j += 1
                else:
                    i -= 1
            return count

        while low < high:
            mid = (low + high) // 2
            count = countLessEqual(mid)
            if k <= count:
                high = mid
            else:
                low = mid + 1

        return low