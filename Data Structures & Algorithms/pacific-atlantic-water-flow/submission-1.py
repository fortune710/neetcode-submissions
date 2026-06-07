from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic_queue = deque()
        pacific_queue = deque()

        atlantic = set()
        pacific = set()

        rows, cols = len(heights), len(heights[0])

        ## Get all Pacific and Atlantic Rows
        for col in range(cols):
            pacific_queue.append((0, col))
            pacific.add((0, col))

            atlantic_queue.append((rows - 1, col))
            atlantic.add((rows - 1, col))

        ## Get all Pacific and Atlantic Columns
        for row in range(rows):
            pacific.add((row, 0))
            atlantic.add((row, cols - 1))

            pacific_queue.append((row, 0))
            atlantic_queue.append((row, cols - 1))
        
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while atlantic_queue:
            r, c = atlantic_queue.popleft()

            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < rows and 0 <= nc < cols and
                    (nr, nc) not in atlantic and 
                    heights[nr][nc] >= heights[r][c]
                ):
                    atlantic.add((nr, nc))
                    atlantic_queue.append((nr, nc))

        while pacific_queue:
            r, c = pacific_queue.popleft()

            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < rows and 0 <= nc < cols and
                    (nr, nc) not in pacific and 
                    heights[nr][nc] >= heights[r][c]
                ):
                    pacific.add((nr, nc))
                    pacific_queue.append((nr, nc))

        return [list(cell) for cell in pacific.intersection(atlantic)]

        


