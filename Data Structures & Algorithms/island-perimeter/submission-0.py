class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        def bfs(i: int, j: int):

            nonlocal perimeter
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
                perimeter += 1
                return
            
            if grid[i][j] == -1:
                return

            grid[i][j] = -1

            neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for x, y in neighbors:
                row, col = i + x, j + y

                bfs(row, col)

            

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    bfs(row, col)

        return perimeter