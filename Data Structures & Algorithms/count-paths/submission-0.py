class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        
        def findPath(i: int, j: int):
            if i == 0 and j == 0:
                return 1

            if i < 0 or j < 0 or i >= m or j >= n:
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            option_1 = findPath(i - 1, j)
            option_2 = findPath(i, j - 1)
            result = option_1 + option_2
            cache[(i, j)] = result
            return result

        return findPath(m - 1, n - 1)