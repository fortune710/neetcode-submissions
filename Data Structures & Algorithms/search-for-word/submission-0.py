class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        def backtrack(row: int, col: int, currentIndex: int):
            ## Pruning
            if board[row][col] != word[currentIndex]:
                return False
            
            ## Base Case
            if currentIndex == len(word) - 1:
                return True

            ## Keep track of the letter for undoing purposes
            letter = board[row][col]
            board[row][col] = "."

            neighbors = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for x, y in neighbors:
                nr, nc = row + x, col + y
                if (0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "."):
                    found = backtrack(nr, nc, currentIndex + 1)
                    if found:
                        return True
            board[row][col] = letter

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0] and backtrack(row, col, 0):
                    return True

        return False