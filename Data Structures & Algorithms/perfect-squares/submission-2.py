import sys
sys.setrecursionlimit(20000)

class Solution:
    def numSquares(self, n: int) -> int:
        stop = int(n ** 0.5)
        nums = [i ** 2 for i in range(1, stop + 1)]
        cache = {}

        def count(remaining: int):
            if remaining == 0:
                return 0

            if remaining < 0:
                return float('inf')

            if remaining in cache:
                return cache[remaining]

            res = float('inf')
            for square in nums:
                # Optional optimization: don't even call if square > remaining
                if square > remaining:
                    break
                
                sub_res = count(remaining - square)
                if sub_res != float('inf'):
                    res = min(res, 1 + sub_res)

            cache[remaining] = res
            return res

        return count(n)