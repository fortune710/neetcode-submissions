class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        cache = {}
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        def findPath(i: int, j: int):
            if i == 0 and j == 0:
                return 1

            if i < 0 or i >= rows or j < 0 or j >= cols or obstacleGrid[i][j] == 1:
                return 0

            cache_key = (i, j)
            if cache_key in cache:
                return cache[cache_key]

            option_1 = findPath(i, j - 1)
            option_2 = findPath(i - 1, j)
            result = option_1 + option_2
            cache[cache_key] = result
            return result

        return findPath(rows - 1, cols - 1)

            