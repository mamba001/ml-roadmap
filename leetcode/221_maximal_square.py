class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        res = 0
        for i in range(m):
            dp[i][0] = 1 if matrix[i][0] == '1' else 0
            res = max(res, dp[i][0])

        for j in range(n):
            dp[0][j] = 1 if matrix[0][j] == '1' else 0
            res = max(res, dp[0][j])

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i -1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    res = max(res, dp[i][j])

        return res ** 2