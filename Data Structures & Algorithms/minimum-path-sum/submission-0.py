class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        cache = {}
        m = len(grid)
        n = len(grid[0])

        def findPathSum(i: int, j: int):
            if i == 0 and j == 0:
                return grid[m - 1][n - 1]

            if i < 0 or i >= m or j < 0 or j >= n:
                return float('inf')

            key = (i, j)
            if key in cache:
                return cache[key]

            option_1 = grid[i - 1][j] + findPathSum(i - 1, j)
            option_2 = grid[i][j - 1] + findPathSum(i, j - 1)
            result = min(option_1, option_2)
            cache[key] = result
            return result
        
        return findPathSum(m - 1, n - 1)