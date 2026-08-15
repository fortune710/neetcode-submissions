class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1Len = len(text1)
        text2Len = len(text2)
        grid = [[0 for _ in range(text2Len)] for _ in range(text1Len)]

        for i in range(text1Len):
            for j in range(text2Len):
                if text1[i] == text2[j]:
                    grid[i][j] = grid[i-1][j-1] + 1 if i > 0 and j > 0 else 1
                else:
                    grid[i][j] = max(grid[i-1][j], grid[i][j-1])

        return grid[text1Len - 1][text2Len - 1]