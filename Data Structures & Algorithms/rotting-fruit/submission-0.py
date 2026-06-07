from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROTTEN, FRESH = 2, 1
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        time = 0

        ##Get all Rotten oranges into queue
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == ROTTEN:
                    queue.append((row, col))
        
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        ## Perform BFS on Rotten Fruit
        while queue:
            level_size = len(queue)
            rotted = False
            for i in range(level_size):
                r, c = queue.popleft()

                for dr, dc in neighbors:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == FRESH:
                            grid[nr][nc] = ROTTEN
                            queue.append((nr, nc))
                            rotted = True

            if rotted:
                time += 1


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == FRESH:
                    return -1

        return time



                

