class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        to_return = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    dp[i][j] = 1
                    if i > 0 and j > 0:
                        dp[i][j] = min(dp[i-1][j], dp[i-1][j-1],dp[i][j-1])+1
                    to_return = max(to_return, dp[i][j] ** 2)
        return to_return