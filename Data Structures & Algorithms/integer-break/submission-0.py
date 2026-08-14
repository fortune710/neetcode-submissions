class Solution:
    def integerBreak(self, n: int) -> int:
        cache = {}
        nums = [i for i in range(1, n)]

        def breakNumber(remaining: int):
            if remaining == 0:
                return 1

            if remaining in cache:
                return cache[remaining]

            result = max(num * breakNumber(remaining - num) for num in range(1, remaining + 1))
            cache[remaining] = result
            return result

        return max(num * breakNumber(n - num) for num in range(1, n))