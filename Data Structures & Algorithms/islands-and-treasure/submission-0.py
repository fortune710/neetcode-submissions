from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        ## Get All The Treaure Chests Into the Queue
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row, col))

        ## Run a BFS
        while queue:
            r, c = queue.popleft()
            neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for nr, nc in neighbors:
                new_row, new_col = r + nr, c + nc
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if grid[new_row][new_col] == INF:
                        grid[new_row][new_col] = grid[r][c] + 1
                        queue.append((new_row, new_col))