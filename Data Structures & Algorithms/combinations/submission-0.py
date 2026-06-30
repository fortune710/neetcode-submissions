class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(index: int, path: List[int]):
            if len(path) == k:
                result.append(path[:])
                return

            if (n - index + 1) < (k - len(path)):
                return

            for idx in range(index, n + 1):
                path.append(idx)
                backtrack(idx + 1, path)
                path.pop()

        backtrack(1, [])
        return result
