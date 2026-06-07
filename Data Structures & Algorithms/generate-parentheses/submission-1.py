class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(open_count: int, closed_count: int, path: List[str]):
            if len(path) == 2 * n:
                result.append("".join(path))
                return
            
            if open_count < n:
                path.append("(")
                backtrack(open_count + 1, closed_count, path)
                path.pop()

            if closed_count < open_count:
                path.append(")")
                backtrack(open_count, closed_count + 1, path)
                path.pop()

        backtrack(0, 0, [])
        return result
